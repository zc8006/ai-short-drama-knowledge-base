from pathlib import Path
import json,wave,subprocess,html
p=Path(__file__).resolve().parent
d=json.loads((p/'分镜与对白.json').read_text(encoding='utf-8'))
rate=22050; output=bytearray();cursor=0;captions=[]
def silence(seconds): return b'\0\0'*round(seconds*rate)
for s in d['shots']:
    s['actual_start']=cursor
    clips=[]
    for line in s['dialogue']:
        with wave.open(str(p/line['wav']),'rb') as w:
            assert w.getframerate()==rate and w.getnchannels()==1 and w.getsampwidth()==2
            raw=w.readframes(w.getnframes())
        clips.append((line,raw))
    spoken=sum(len(raw)/(rate*2) for _,raw in clips)
    duration=max(s['planned_duration'],spoken+.45*len(clips)+.8)
    padding=duration-spoken-.35*max(0,len(clips)-1)
    output.extend(silence(padding*.3));local=cursor+padding*.3
    for i,(line,raw) in enumerate(clips):
        length=len(raw)/(rate*2)
        captions.append({'start':local,'end':local+length,'role':line['role'],'text':line['text']})
        output.extend(raw);local+=length
        if i<len(clips)-1: output.extend(silence(.35));local+=.35
    output.extend(silence(padding*.7))
    cursor+=duration;s['actual_duration']=duration
with wave.open(str(p/'声音预演_临时配音.wav'),'wb') as w:
    w.setparams((1,2,rate,0,'NONE','not compressed'));w.writeframes(output)
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(p/'声音预演_临时配音.wav'),'-codec:a','libmp3lame','-q:a','3',str(p/'声音预演_临时配音.mp3')],check=True)
d['actual_duration']=cursor;d['captions']=captions
(p/'声音时间轴.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
def tc(v):
    n=round(v*1000);return f'{n//3600000:02}:{n//60000%60:02}:{n//1000%60:02},{n%1000:03}'
(p/'对白.srt').write_text('\n\n'.join(f"{i+1}\n{tc(c['start'])} --> {tc(c['end'])}\n{c['role']}：{c['text']}" for i,c in enumerate(captions)),encoding='utf-8-sig')
page='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>这次，是邀请你 · 分镜声音预演</title><style>
*{box-sizing:border-box}body{margin:0;background:#101519;color:#eee9df;font:17px/1.7 "Microsoft YaHei",sans-serif}main{max-width:1100px;margin:40px auto;padding:24px}small{color:#b7a178;letter-spacing:3px}h1{font-size:38px;font-weight:500}p{color:#bfc5c8}.panel{border:1px solid #38414a;padding:35px;background:#172028;min-height:300px;border-radius:10px}#action{max-width:760px;font-size:24px;color:#ddd}#caption{min-height:65px;margin-top:30px;font-size:27px;color:#e7c993}audio{width:100%;margin:25px 0}nav{display:flex;flex-wrap:wrap;gap:8px}button{background:#26333f;border:1px solid #4b5964;color:#eee;padding:9px 13px;cursor:pointer;border-radius:4px}button.active{background:#76613d}.note{font-size:14px}</style>
<main><small>NOVEL ADAPTATION / EP01</small><h1>这次，是邀请你</h1><p>分镜声音预演 · 临时系统配音 · 尚无新生成的人物画面</p><section class="panel"><small id="shot"></small><div id="action"></div><div id="caption"></div></section><audio id="audio" controls src="声音预演_临时配音.mp3"></audio><nav id="nav"></nav><p class="note">点击镜头可跳转。声音留白对应表演与反应镜头；此页用于审阅剧情和节奏，不是最终视频。视频计划16:9 / 768p。</p></main><script>
const data=__DATA__;const a=document.getElementById('audio');const buttons=[];for(const s of data.shots){const b=document.createElement('button');b.textContent=s.id+' '+s.frame.split('·')[0];b.onclick=()=>{a.currentTime=s.actual_start;a.play()};document.getElementById('nav').append(b);buttons.push(b)}function update(){const t=a.currentTime;const i=data.shots.findIndex(s=>t>=s.actual_start&&t<s.actual_start+s.actual_duration);const s=data.shots[Math.max(0,i)];document.getElementById('shot').textContent=s.id+' / '+s.frame;document.getElementById('action').textContent=s.action;const c=data.captions.find(c=>t>=c.start&&t<=c.end);document.getElementById('caption').textContent=c?c.role+'：'+c.text:' ';buttons.forEach((b,n)=>b.classList.toggle('active',n===i))}a.addEventListener('timeupdate',update);update();</script></html>'''
(p/'分镜声音预演.html').write_text(page.replace('__DATA__',json.dumps(d,ensure_ascii=False).replace('</','<\\/')),encoding='utf-8')
(p/'00_制作状态.md').write_text(f'''# 制作状态

已完成：小说第165—166章核对、12镜头拍摄剧本、{len(captions)}句对白、生成提示词、临时声音预演、SRT字幕和可播放的分镜审阅页。声音预演实际约{cursor:.1f}秒。

未完成：三名角色定妆、正式人物视频、自然表演配音、音乐、剪辑成片。没有提交新的视频生成或扣费任务。

下一步：连接用户选定的视频生成平台，锁定人物与教室；优先做S09和S11，验证真心表白与回应。每次提交前核对768p。不要重复生成旧S05任务，也不使用旧参考剧情视频填充新故事。

原文关系：高尔是由马尔福安排的优秀陪练；偷听及本版对白是改编。原文核心是哈利愿意做伴舞者，让她领舞。源小说文件未改动。
''',encoding='utf-8')
print(json.dumps({'duration':cursor,'shots':len(d['shots']),'lines':len(captions),'audio_bytes':(p/'声音预演_临时配音.mp3').stat().st_size},ensure_ascii=False))

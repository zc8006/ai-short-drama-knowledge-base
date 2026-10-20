from pathlib import Path
import json,subprocess
root=Path.cwd();plan=json.loads((root/'timeline.json').read_text(encoding='utf-8'))
flags=0x08000000

def run(cmd):subprocess.run(['ffmpeg','-hide_banner','-loglevel','error',*cmd],check=True,creationflags=flags)
run(['-f','lavfi','-i','color=c=0x111917:s=1366x768:r=24:d=2.5','-an','-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p','-y','assets/end-card.mp4'])
(root/'clips.txt').write_text(''.join("file '"+c['file']+"'\n" for c in plan['clips'])+"file 'assets/end-card.mp4'\n",encoding='utf-8')
run(['-f','concat','-safe','0','-i','clips.txt','-c','copy','-y','assets/picture.mp4'])
def ass_time(v):
 centis=round(v*100);return f'{centis//360000}:{centis//6000%60:02}:{centis//100%60:02}.{centis%100:02}'
head='''[Script Info]
ScriptType: v4.00+
PlayResX: 1366
PlayResY: 768
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Subtitle,Microsoft YaHei,42,&H00F4F3EA,&H00FFFFFF,&H00101514,&H00101514,0,0,0,0,100,100,1,0,1,1.3,0,2,55,55,55,1
Style: Small,Microsoft YaHei,23,&H00D1DED8,&H00FFFFFF,&H80202B24,&H00101514,0,0,0,0,100,100,1,0,1,1,0,7,45,45,28,1
Style: Title,Microsoft YaHei,69,&H00F4F3EA,&H00FFFFFF,&H00101514,&H00101514,1,0,0,0,100,100,3,0,1,0,0,5,60,60,30,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
'''
events=[]
def add(start,end,style,text):events.append(f'Dialogue: 0,{ass_time(start)},{ass_time(end)},{style},,0,0,0,,{text}')
add(0,plan['picture_duration'],'Small',r'{\an7\pos(42,30)}参考剪辑预演  ·  临时配音 / 未对口型')
for c in plan['clips']:
 start=c['audio_start'];end=min(c['start']+c['duration'],start+3.0)
 color='&H9ECDBE&' if c['character']=='德拉科' else '&HB1D8EA&'
 add(c['start']+.05,c['start']+c['duration'],'Small',r'{\an5\pos(683,641)\c'+color+'}'+c['character'])
 add(start,end,'Subtitle',r'{\an5\pos(683,695)}'+c['subtitle'])
start=plan['picture_duration'];end=plan['duration']
add(start,end,'Small',r'{\an5\pos(683,255)}舞会篇  ·  核心反转预演')
add(start,end,'Title',r'{\an5\pos(683,357)}她答应得太早了')
add(start,end,'Small',r'{\an5\pos(683,515)}小说背景：Luis没了  ｜  参考画面：允希 YUNXI')
add(start,end,'Small',r'{\an5\pos(683,565)}对白为改编新写；正式人物动作底片尚未生成')
(root/'captions.ass').write_text(head+'\n'.join(events)+'\n',encoding='utf-8-sig')
args=['-i','assets/picture.mp4']
for c in plan['clips']:args+=['-i',f"audio/{c['line_id']}.wav"]
args+=['-f','lavfi','-i',f"anoisesrc=color=brown:amplitude=0.025:sample_rate=48000:duration={plan['duration']}"]
filters=[]
for i,c in enumerate(plan['clips'],1):
 delay=round(c['audio_start']*1000)
 filters.append(f'[{i}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={delay}|{delay}[v{i}]')
filters.append('[8:a]highpass=f=90,lowpass=f=900,volume=0.1,aformat=channel_layouts=stereo[room]')
filters.append(''.join(f'[v{i}]' for i in range(1,8))+'[room]amix=inputs=8:duration=longest:normalize=0,loudnorm=I=-18:TP=-1.5:LRA=7,afade=t=in:d=0.05,afade=t=out:st=19.375:d=0.5[mix]')
filters.append('[0:v]drawbox=x=0:y=610:w=iw:h=158:color=0x101514:t=fill,ass=captions.ass[v]')
args+=['-filter_complex',';'.join(filters),'-map','[v]','-map','[mix]','-t',str(plan['duration']),'-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-ar','48000','-b:a','192k','-movflags','+faststart','-y','参考剪辑预演_v01_768p.mp4']
run(args)
print('Rendered',root/'参考剪辑预演_v01_768p.mp4')

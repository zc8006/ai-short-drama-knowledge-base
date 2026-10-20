from pathlib import Path
import json, html

ROOT=Path(__file__).resolve().parent/'样片_EP01_这次是邀请你'
ROOT.mkdir(exist_ok=True)
(ROOT/'audio').mkdir(exist_ok=True)
shots=[
('S01',6,'走廊·双人中景','哈利鼓起勇气开口；马尔福忍住笑，等着下一句。',[('哈利','马尔福，你愿不愿意……'),('马尔福','可以。')]),
('S02',5,'马尔福近景→哈利反打','她先答应，随后才听见请求。期待凝住，不做夸张变脸。',[('哈利','教我跳舞？'),('马尔福','……你就想问这个？')]),
('S03',7,'魔药学教室·固定全景','桌椅移到两旁。她指向站姿端正的高尔；哈利以为要与她跳，伸出的手停在半空。',[('马尔福','先跟高尔练。'),('哈利','跟他？')]),
('S04',8,'舞步与面部切换','高尔示范糟糕领舞，哈利被迫追步。第二次示范平稳优雅，表现高尔有真本领。',[('马尔福','先学会跟随，才知道舞伴是什么感受。')]),
('S05',6,'教室·两人对视','她状似随口地问，实际上认真等待。他一紧张，只顾脚下。',[('马尔福','你准备邀请谁？'),('哈利','我想先练好。')]),
('S06',5,'马尔福特写·落空','她垂眼收起折扇，退出练习区。哈利没有及时追问。',[('马尔福','那你慢慢练。')]),
('S07',6,'夜·门外→门内','字幕“一周后”。她经过教室，听见高尔计数；停步，尚不入镜。',[('高尔','一、二、三。又来？'),('哈利','再来一次。')]),
('S08',7,'高尔中近景→哈利','高尔松开架势，认真地问，不演成嘲笑。',[('高尔','你直接邀请她不就好了？'),('哈利','我不想让她在舞会上出糗。')]),
('S09',7,'哈利近景→门外马尔福','哈利回到起步位置；门外她听见自己的名字，肩膀慢慢放松。',[('哈利','我想邀请的，一直是马尔福。')]),
('S10',8,'教室门口·双人中景','稍后，高尔离开。她走进来。哈利站直，正式伸手。',[('哈利','马尔福小姐，愿意做我的舞伴吗？')]),
('S11',8,'马尔福近景→哈利','她不急着伸手，要确认这一次的意义。他终于正面回答。',[('马尔福','这次，是学跳舞，还是邀请我？'),('哈利','邀请你。你来领舞，也可以。')]),
('S12',7,'手部→中景收尾','她把手放进他的掌心，带出第一步。他顺着节拍跟上，只完成一次简单侧步。',[('马尔福','那就跟紧我，别踩我的脚。')]),
]
data={'title':'这次，是邀请你','status':'制作分镜与临时声音预演；尚无新生成的人物视频','resolution':'768p','aspect':'16:9','source':'Luis没了《笨蛋哈利与马尔福大小姐的二三事》第165—166章，CH-0164、CH-0165','shots':[]}
lines=[]; t=0
for sid,dur,frame,action,dialog in shots:
    ds=[]
    for role,txt in dialog:
        lid=f'L{len(lines)+1:02}'
        d={'id':lid,'role':role,'text':txt,'wav':f'audio/{lid}.wav'}
        ds.append(d);lines.append(d)
    data['shots'].append({'id':sid,'planned_start':t,'planned_duration':dur,'frame':frame,'action':action,'dialogue':ds})
    t+=dur
data['planned_duration']=t
(ROOT/'分镜与对白.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'对白.json').write_text(json.dumps(lines,ensure_ascii=False,indent=2),encoding='utf-8')
md=['# 《这次，是邀请你》制作版 v01','',f'计划时长：{t}秒。横版16:9，视频生成默认768p。','',
'## 叙事与表演','',
'前段是请求错位，中段让她以为自己只是帮忙的人，后段用练习中的真心回应她。结尾她领舞、他跟随，让“配合舞伴”成为这段感情的动作表达。',
'','高尔是认真的好舞者，不拿他的身材或男性共同练舞作羞辱笑料。她的失落通过视线、停顿表现；哈利的笨拙是没说清心意，不是故意吊着她。','',
'## 原文与改编边界','',
'小说事实：先请教跳舞引起误会；马尔福安排高尔陪练，先让哈利体验伴舞者感受；一周训练后哈利正式邀舞；他解释不想让她出糗，并愿意让她领舞。',
'','新增改编：她问舞伴是谁、短暂离开、门外偷听他与高尔对话，以及本版具体台词。原文不是高尔秘密代替马尔福教舞；本版仍保留她安排教学这一事实。',
'','省略原文与本场叙事无关的亲密描写。本版是校园邀舞，不采用性感化服饰或动作。','',
'## 分镜与对白','']
for s in data['shots']:
    md += [f"### {s['id']}｜{s['planned_start']}—{s['planned_start']+s['planned_duration']}秒｜{s['frame']}",'',s['action'],'']
    md += [f"{d['role']}：{d['text']}" for d in s['dialogue']]
    md += ['']
md+=['## 素材状态','','已有：剧本、12段分镜、对白表、提示词。临时配音由本地系统语音生成，仅核对节奏，不代表最终人物声音。正式人物画面、人物定妆及音乐尚未制作。旧版参考视频不拼入本版。']
(ROOT/'01_拍摄剧本.md').write_text('\n'.join(md),encoding='utf-8')
base='电影写实风格，非演员复刻。霍格沃茨校园，冷蓝窗光与暖色壁灯；自然皮肤、克制表演，端庄校服，无文字无水印。哈利：黑色凌乱短发、圆眼镜、格兰芬多红金领带；女性德拉科：白金长发、斯莱特林绿银领带，骄傲但不刻薄。高尔：宽肩体格、稳重、有良好的社交舞姿态，绿银领带。三人是同龄学生，妆造与年龄相符。人物面孔、发型与左右站位保持连续；生成画面不负责口型对白，后期配音。'
prompts=['# 镜头生成单','','状态：未提交。先锁定三人定妆图与教室场景，再制作核心镜头。每次提交都检查实际设置为768p；切换模型后再次检查。时长、报价以实际界面为准，不在缺少报价时承诺总费用。', '',base,'','优先验证S09与S11：真心说出口，以及她愿意接住邀请。先获得可用人物画面，再扩展全片。单条只生成一个动作，复杂跳舞拆成手部、脚步和面部反应。不要要求模型一次生成完整12镜头。','']
for s in data['shots']:
    prompts += [f"## {s['id']}｜剪辑目标{s['planned_duration']}秒",'',f"构图：{s['frame']}。动作：{s['action']}。仅做该动作，不添加额外人物、亲吻、摔倒或夸张表情。运镜以固定机位或非常缓慢推进为主。",'']
(ROOT/'02_镜头生成单.md').write_text('\n'.join(prompts),encoding='utf-8')
ps='''$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$taskRoot = $PSScriptRoot
$taskLines = Get-Content -LiteralPath (Join-Path $taskRoot '对白.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$taskSynth = New-Object System.Speech.Synthesis.SpeechSynthesizer
foreach ($taskLine in $taskLines) {
  $taskVoice = if ($taskLine.role -eq '马尔福') { 'Microsoft Yaoyao' } else { 'Microsoft Kangkang' }
  $taskSynth.SelectVoice($taskVoice)
  $taskSynth.Rate = if ($taskLine.role -eq '高尔') { -1 } else { 0 }
  $taskSynth.SetOutputToWaveFile((Join-Path $taskRoot $taskLine.wav))
  $taskSynth.Speak($taskLine.text)
  $taskSynth.SetOutputToNull()
}
$taskSynth.Dispose()
'''
(ROOT/'生成临时配音.ps1').write_text(ps,encoding='utf-8-sig')
print(ROOT)

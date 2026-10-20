from pathlib import Path
import json,subprocess,math
root=Path(__file__).resolve().parent
source=Path('<LOCAL_RESOURCE_PATH>')
items=[('S01',1.0,4.6,'L01',.25),('S02',6.0,9.1,'L02',.18),('S03',22.75,25.05,'L03',.15),('S04',18.0,19.7,'L04',.12),('S05',11.2,13.4,'L05',.15),('S06',9.1,11.2,'L06',.01),('S07',13.4,15.8,'L07',.1)]
lines={x['id']:x for x in json.loads((root/'对白.json').read_text(encoding='utf-8-sig'))}
clips=[];start=0
for name,a,b,lid,delay in items:
 duration=round((b-a)*24)/24
 cmd=['ffmpeg','-hide_banner','-loglevel','error','-ss',str(a),'-i',str(source),'-t',str(duration),'-an','-vf','scale=1366:768:flags=lanczos,fps=24,setsar=1','-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p','-y',str(root/'assets'/f'{name}.mp4')]
 subprocess.run(cmd,check=True)
 clips.append(dict(id=name,source_start=a,source_end=b,start=start,duration=duration,line_id=lid,audio_start=start+delay,subtitle=lines[lid]['text'],character=lines[lid]['character'],file=f'assets/{name}.mp4'))
 start+=duration
(root/'timeline.json').write_text(json.dumps(dict(kind='reference_edit_animatic',source_video=str(source),source_author='允希 YUNXI',width=1366,height=768,fps=24,clips=clips,picture_duration=start,end_card_duration=2.5,duration=start+2.5),ensure_ascii=False,indent=2),encoding='utf-8')
print('PICTURE',start,'TOTAL',start+2.5)

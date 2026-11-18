"""按实片帧点生成 EP02 全集粗剪，保留可复核的剪辑单。"""

import argparse
import concurrent.futures
import json
import subprocess
import tempfile
from pathlib import Path


FPS = 24
EPISODE = Path(__file__).resolve().parents[1]
OUTPUT = Path(__file__).resolve().parent
FONT = "C\\:/Windows/Fonts/msyh.ttc"
CUTS = []


def add(name, source, start, end, **options):
    start_frame = round(start * FPS)
    end_frame = round(end * FPS)
    CUTS.append(dict(name=name, source=source, start=start_frame / FPS,
                     frames=end_frame - start_frame, **options))


add("浓烟铁门与白栖赶到", "EP001.mp4", 0, 6.208333)
add("当天早上", None, 0, 0.75, card="当天早上")
add("白璐的旧采访笔记", "插镜素材/EP02-001_白璐旧笔记_月考疑问_韩文.png", 0, 2.75,
    still=True, label="白璐的旧采访笔记", ambient=("EP001.mp4", 7.75, 9.75))
add("姜书沅公布巡逻", "EP001.mp4", 7.75, 11.958333)
add("走廊低声提醒补拍", "E02_001补拍.mp4", 0, 5.041667)
add("白栖回应与盲区图、跟班打火机", "EP001.mp4", 16.291667, 21.875)
add("白栖收图眼神", "EP001.mp4", 22.5, 25.041667)

add("午后空座问路、寻人及入室", "试剪/EP02-002_三条补拍试剪_v1.mp4", 0, 16.625,
    label="当天午后", label_seconds=1.2, chapter="rescue")
add("拉阀与刚落下的水", "补拍视频/02_红柜喷淋与弯发卡_节奏试剪_v3.mp4", 0.875, 1.666667)
add("锁孔留下弯发卡", "补拍视频/02_红柜喷淋与弯发卡_节奏试剪_v3.mp4", 1.958333, 3.208333)
add("扶人跨出门槛", "补拍视频/002补拍4.mp4", 0, 5.041667,
    audio_tail=("试剪/EP02-002_三条补拍试剪_v1.mp4", 22.0, 22.458333))
add("门外叙述、白璐往事、捡火机与独白", "试剪/EP02-002_三条补拍试剪_v1.mp4", 22.458333, 38.333333)

add("浓烟通报与学生检查员示意", "补拍视频/02_003_补拍3_开场查包.mp4", 0, 4.041667, chapter="checkpoint")
add("跟班慌张、南智宥动机与白栖抱书走来", "EP02-003.mp4", 2.75, 8.583333)
add("错身与袋口露出火机", "补拍视频/02_003_补拍1_托特包袋口.mp4", 0.708333, 2.916667)
add("搜出同一打火机、处置跟班与白栖袖口", "EP02-003.mp4", 12.708333, 18.125)
add("南智宥急辩失言后合嘴", "补拍视频/02_003_补拍2_南智宥失言.mp4", 0.25, 3.416667)
add("姜书沅转头、扣分与白栖反应", "EP02-003.mp4", 19.791667, 26.041667)

add("放学楼梯质问", "EP02-004.mp4", 0, 15,
    label="放学后", label_seconds=1.3, chapter="after_school")
add("权限表指向副校长室", "插镜素材/EP02-004_权限表_副校长室_韩文注释.png", 0, 2.75,
    still=True, audio_source=("EP02-004.mp4", 15, 17.041667))
add("白栖夜间补记答案", "插镜素材/EP02-004_白栖补记_封装负责人_韩文.png", 0, 3,
    still=True, audio_source=("EP02-004.mp4", 17.041667, 19))
add("银饰手操纵鼠标", "EP02-004.mp4", 19, 20.458333)
add("后台选中白栖", "EP02-004.mp4", 20.458333, 21.791667,
    filter="drawbox=x=121:y=429:w=360:h=58:color=0x01121e:t=fill")
add("白栖被列入红名单", "EP02-004.mp4", 21.791667, 24,
    filter="drawbox=x=118:y=210:w=602:h=155:color=0x01121e:t=fill")
add("片尾黑卡", "EP02-004.mp4", 24, 26.041667)


def run(arguments):
    result = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *arguments],
                            capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode:
        raise RuntimeError(result.stderr)


def make_segment(index, cut, work):
    duration = cut["frames"] / FPS
    target = work / f"{index:03}.mkv"
    args = []
    source = EPISODE / cut["source"] if cut["source"] else None
    if cut.get("card"):
        args += ["-f", "lavfi", "-i", "color=c=black:s=720x1280:r=24"]
    elif cut.get("still"):
        args += ["-loop", "1", "-framerate", "24", "-i", str(source)]
    else:
        args += ["-ss", str(cut["start"]), "-i", str(source)]

    video_filter = "fps=24,scale=720:1280:flags=lanczos,setsar=1"
    if cut.get("still"):
        video_filter += (",scale=1440:2560:flags=lanczos,"
                         f"zoompan=z='1+0.012*on/{cut['frames']}':"
                         "x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=1:s=720x1280:fps=24")
    if cut.get("filter"):
        video_filter += "," + cut["filter"]
    if cut.get("label") or cut.get("card"):
        text = cut.get("card") or cut["label"]
        position = "y=(h-th)/2" if cut.get("card") else "y=100"
        font_size = 46 if cut.get("card") else 30
        video_filter += (f",drawtext=fontfile='{FONT}':text='{text}':fontsize={font_size}:"
                         f"fontcolor=white:borderw=2:bordercolor=black@0.5:x=(w-tw)/2:{position}")
        if cut.get("label_seconds"):
            video_filter += f":enable='lt(t,{cut['label_seconds']})'"
    video_filter += ",format=yuv420p,setpts=PTS-STARTPTS"

    if cut.get("audio_tail"):
        name, begin, end = cut["audio_tail"]
        tail_duration = end - begin
        delay = duration - tail_duration
        args += ["-ss", str(begin), "-i", str(EPISODE / name)]
        audio = (f"[0:a]atrim=duration={delay},asetpts=PTS-STARTPTS,"
                 "aresample=48000,aformat=channel_layouts=stereo[a0];"
                 f"[1:a]atrim=duration={tail_duration},asetpts=PTS-STARTPTS,"
                 "aresample=48000,aformat=channel_layouts=stereo[a1];"
                 "[a0][a1]concat=n=2:v=0:a=1[ac]")
    elif cut.get("audio_source") or cut.get("ambient"):
        name, begin, end = cut.get("audio_source") or cut["ambient"]
        args += ["-ss", str(begin), "-i", str(EPISODE / name)]
        gain = ",volume=0.22" if cut.get("ambient") else ""
        audio = (f"[1:a]atrim=duration={end-begin},asetpts=PTS-STARTPTS,"
                 f"aresample=48000,aformat=channel_layouts=stereo{gain},apad[ac]")
    elif cut.get("card"):
        args += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
        audio = "[1:a]anull[ac]"
    else:
        audio = "[0:a]aresample=48000,aformat=channel_layouts=stereo,asetpts=PTS-STARTPTS[ac]"

    graph = (f"[0:v]{video_filter}[v];{audio};"
             f"[ac]apad,atrim=duration={duration},"
             f"afade=t=in:d=0.004,afade=t=out:st={max(0,duration-0.004)}:d=0.004[a]")
    args += ["-filter_complex_threads", "1", "-filter_complex", graph,
             "-map", "[v]", "-map", "[a]", "-t", str(duration),
             "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-threads", "2",
             "-c:a", "pcm_s16le", "-ar", "48000", str(target)]
    run(args)
    print(f"{index+1:02}/{len(CUTS)} {cut['name']}", flush=True)
    return target


def write_sheet():
    total = 0.0
    lines = ["# 《温柔的獠牙》EP02 全集粗剪 v1", "",
             "2026-11-18。720 × 1280、24 fps，按现有实片剪接。保留原对白及内心独白，沿用无 BGM 设计。新增当天早上、当天午后、放学后提示和三张线索插镜的文字。", "",
             "救火处理为短暂拉阀及初落水、锁孔发卡、完整扶行撤离。通过压短喷水表演减少违和，原素材的消防装置呈现仍待观感复核。", "",
             "源时码与入出点见下列条目。时间为源文件秒数，入出点按 24 fps 对齐，输出位置为预计值。音频原声随画面走，撤离末尾提前接入原片门外台词，避免丢起音。", ""]
    for index, cut in enumerate(CUTS, 1):
        duration = cut["frames"] / FPS
        cut["timeline_start"] = total
        lines.extend([f"## CUT-EP02-{index:03} · {cut['name']}", "",
                      f"- 来源文件 {cut['source'] or '后期黑底时间卡'}",
                      f"- 源入点 {cut['start']:.3f} 秒，源出点 {cut['start']+duration:.3f} 秒",
                      f"- 片长 {duration:.3f} 秒，全集位置 {total:.3f}–{total+duration:.3f} 秒", ""])
        total += duration
    lines.extend(["## 本版取舍与待复核", "",
                  "- 001 走廊旧镜被补拍替换，原末段显露黄色物件的开头裁掉约 0.625 秒，保留最终眼神。",
                  "- 002 复用三条补拍试剪 v1，压短拉阀与落水，加入 002补拍4 的跨门槛动作。金多贞的原门外台词起音提前约 0.458 秒铺在撤离结尾。",
                  "- 003 删去底片 11.25–12.708 秒重复的保安帽检查镜。失言旧台词在画面切镜前提前起音，因此在 18.125 秒切出，避免新旧说话重叠。补拍 2 的人名发音、音色仍待人工回听。",
                  "- 004 权限表与笔记改用韩文静帧及中文释义。后台两机位的错误中文通过局部深色遮罩清理，保留原位置的白栖名字、选中框和红色预警。",
                  "- 原镜对白保留，当前粗剪未加全片对白字幕。三张线索图的中文释义已在图内。",
                  "- 袋口补拍仍有打火机突现感，三张静帧与原视频的接点、消防表演、发卡形态和门外对话换边须看本版成片复核。", "",
                  f"预计总长 {total:.3f} 秒。导出后以 ffprobe 实测为准。", ""])
    (OUTPUT / "EP02_粗剪_v1_剪辑单.md").write_text("\n".join(lines), encoding="utf-8")
    (OUTPUT / "EP02_粗剪_v1_时间线.json").write_text(json.dumps(CUTS, ensure_ascii=False, indent=2), encoding="utf-8")
    return total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan-only", action="store_true")
    args = parser.parse_args()
    for cut in CUTS:
        if cut["source"] and not (EPISODE / cut["source"]).is_file():
            raise FileNotFoundError(cut["source"])
    total = write_sheet()
    print(f"Timeline {total:.3f} seconds", flush=True)
    if args.plan_only:
        return
    target = OUTPUT / "温柔的獠牙_EP02_全集粗剪_v1.mp4"
    if target.exists():
        raise FileExistsError(target)
    with tempfile.TemporaryDirectory(prefix="ep02_render_") as temp:
        work = Path(temp)
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            futures = [pool.submit(make_segment, i, cut, work) for i, cut in enumerate(CUTS)]
            segments = [future.result() for future in futures]
        concat = work / "concat.txt"
        concat.write_text("\n".join(f"file '{path.as_posix()}'" for path in segments), encoding="utf-8")
        run(["-f", "concat", "-safe", "0", "-i", str(concat), "-map", "0:v", "-map", "0:a",
             "-c:v", "copy", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11,volume=-1.2dB", "-c:a", "aac",
             "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", str(target)])
    print(str(target), flush=True)


if __name__ == "__main__":
    main()

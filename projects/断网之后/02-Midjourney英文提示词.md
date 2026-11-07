# 《断网之后，全网跪求老架构师》｜Midjourney英文资产提示词

适用：阶段2全季资产库，6集，AI仿真人影视风。  
依据：2026-11-04当前《02-全季资产库》，保留原人物、服装、道具和空间关系。  
交付：中文索引与使用说明＋可复制英文正文。此文档为独立适配版，原企划与中文资产库未改写；未执行图片生成。

## 先这样试

1. 先复制 **IMG-P01-PORTRAIT（周衍正面半身）**，在Midjourney网页的Imagine输入框生成，挑一张满意的脸。
2. 再试 **IMG-STYLE01（风格定调）** 看真人摄影、冷暖色和材质方向；人物定妆仍以选定的单人图为准。
3. 在V8.2网页将选中的人物图附到 **Attach to prompt**，再粘贴对应全身、湿衣、表情或三视图正文。参考图控制身份；提示词控制当前衣服、表情与构图。
4. 三视图是可选辅助图。建议脸确认后再做；如侧背面换脸，拆成单张编辑，不把三个人形直接用作视频首帧。
5. 复制的内容从英文首句到末尾参数，不复制中文标题、引用符号或文件编号。网页不用输入`/imagine`；Discord先调用`/imagine`，再贴正文。

参数按2026-11-04查询的官方文档适配V8.2。每条已附`--ar`、`--raw`、`--s`、`--v 8.2`与`--no`，参数集中在末尾；不用再叠加另一套负面参数。`--s 50`是本项目试图起点，不是成功保证。若当前界面仅提供其他版本，应先切换到V8.2再直接使用本版。

| 参数／功能 | 本版用法 |
|---|---|
| `--ar 9:16` | 单人定妆、表情、场景和特效，竖屏 |
| `--ar 16:9` | 人物三视图、电脑、车辆等参考板；正片仍为9:16 |
| `--ar 1:1` | 小道具 |
| `--raw` | 减少MJ默认风格介入；配合photorealistic、live-action和真实皮肤描述 |
| `--s 50` | 人物和场景先低风格化试图；道具用25，风格帧用75 |
| V8.2参考图 | 网页Attach to prompt进入Edit模型路线；当前官方支持最多4张参考图。本文不拼入旧版`--cref`或`--oref`参数。 |
| 风格参考 | STYLE01只控制摄影风格、色彩、材质；不要让它替换人物脸或场景空间。Style Reference与人物身份参考分开使用。 |

所有英文正文不依赖人名识脸，采用年龄、面部锚点、身高和服装描述；“秦岚”等角色名只用于中文检索，不指定同名真实演员。纯文字生成不能保证跨图同脸；进入变体时附上已选主图。眼镜、手表左右腕、泥污和接口位置仍需检查。

## 目录与生成顺序

| 类别 | 内容 |
|---|---|
| STYLE01 | 真人影视风格定调 |
| P01–P06 | 6张单人正面半身、6套主卡三视图、全身服装与状态、24张表情、跪姿关键状态 |
| G01–G03 | 员工、随行人员、法务／警方群演 |
| D01–D13 | 工牌内芯、旧键盘、保温杯、防弹终端及补充道具的各状态 |
| S01–S06 | 无人空景、正常／警报／恢复光效、剧情机位底板 |
| FX01–FX06 | 雨、车灯、警报光、海雾、火花、盲敲残影 |
| 后期固定表 | UI、编号、合同、倒计时和证据；不让MJ生成文字 |

生成顺序：周衍正面试图→风格帧→6名人物正面定脸→全身与需要的状态→道具→场景→特效。角色后续状态按同一主图派生，不每次从零随机抽脸。画面中的0001、盘古AI、15%、交易金额与倒计时全部后期制作。

## 提示词索引

| 编号 | 中文用途 |
|---|---|
| IMG-STYLE01 | 真人影视风格定调 |
| IMG-P01-PORTRAIT | 周衍｜正面半身定脸 |
| IMG-P01-MASTER | 周衍｜三视图主卡 |
| IMG-P01-LOOK-A | 周衍｜基础服装全身 |
| IMG-P01-EXPR-CALM | 周衍｜平静 |
| IMG-P01-EXPR-RESTRAINED | 周衍｜克制 |
| IMG-P01-EXPR-FOCUSED | 周衍｜专注 |
| IMG-P01-EXPR-RELIEVED | 周衍｜释然 |
| IMG-P02-PORTRAIT | 贺凯｜正面半身定脸 |
| IMG-P02-MASTER | 贺凯｜三视图主卡 |
| IMG-P02-LOOK-A | 贺凯｜基础服装全身 |
| IMG-P02-EXPR-CONTEMPT | 贺凯｜轻蔑 |
| IMG-P02-EXPR-SHOCK | 贺凯｜错愕 |
| IMG-P02-EXPR-FEAR | 贺凯｜恐惧 |
| IMG-P02-EXPR-RESENTMENT | 贺凯｜怨恨 |
| IMG-P03-PORTRAIT | 秦岚｜正面半身定脸 |
| IMG-P03-MASTER | 秦岚｜三视图主卡 |
| IMG-P03-LOOK-A | 秦岚｜基础服装全身 |
| IMG-P03-EXPR-ASSESSING | 秦岚｜审视 |
| IMG-P03-EXPR-SHOCK | 秦岚｜震惊 |
| IMG-P03-EXPR-PLEADING | 秦岚｜恳切 |
| IMG-P03-EXPR-RESOLUTE | 秦岚｜坚定 |
| IMG-P04-PORTRAIT | 唐小川｜正面半身定脸 |
| IMG-P04-MASTER | 唐小川｜三视图主卡 |
| IMG-P04-LOOK-A | 唐小川｜基础服装全身 |
| IMG-P04-EXPR-INDIGNANT | 唐小川｜不平 |
| IMG-P04-EXPR-ANXIOUS | 唐小川｜焦急 |
| IMG-P04-EXPR-CERTAIN | 唐小川｜确信 |
| IMG-P04-EXPR-HAPPY | 唐小川｜欣喜 |
| IMG-P05-PORTRAIT | 魏哲｜正面半身定脸 |
| IMG-P05-MASTER | 魏哲｜三视图主卡 |
| IMG-P05-LOOK-A | 魏哲｜基础服装全身 |
| IMG-P05-EXPR-ARROGANT | 魏哲｜倨傲 |
| IMG-P05-EXPR-FLUSTERED | 魏哲｜失措 |
| IMG-P05-EXPR-AWESTRUCK | 魏哲｜震撼 |
| IMG-P05-EXPR-FRIGHTENED | 魏哲｜惊惧 |
| IMG-P06-PORTRAIT | 裴元｜正面半身定脸 |
| IMG-P06-MASTER | 裴元｜三视图主卡 |
| IMG-P06-LOOK-A | 裴元｜基础服装全身 |
| IMG-P06-EXPR-COLD | 裴元｜冷漠 |
| IMG-P06-EXPR-CONFIDENT | 裴元｜笃定 |
| IMG-P06-EXPR-ALERT | 裴元｜警觉 |
| IMG-P06-EXPR-FROZEN | 裴元｜僵硬 |
| IMG-P01-A-W | 周衍｜湿风衣 |
| IMG-P01-LOOK-B | 周衍｜脱风衣挽袖 |
| IMG-P01-B-N | 周衍｜摘镜闭眼 |
| IMG-P02-A-W | 贺凯｜下跪前湿西装 |
| IMG-P02-LOOK-B | 贺凯｜泥膝狼狈态 |
| IMG-P03-A-W | 秦岚｜雨后白西装 |
| IMG-P04-A-L | 唐小川｜值守疲惫 |
| IMG-P05-A-S | 魏哲｜专家失利 |
| IMG-P05-A-W | 魏哲｜雨后狼狈 |
| IMG-P02-KNEEL | 贺凯｜跪递防弹电脑 |
| IMG-P05-KNEEL | 魏哲｜认出Zero后跪拜 |
| IMG-G01 | 值守员工 |
| IMG-G02 | 随行人员 |
| IMG-G03 | 法务／便衣警方群演 |
| IMG-D01-A | 0001工牌｜完整 |
| IMG-D01-B | 0001工牌｜裂壳 |
| IMG-D01-C | 0001内芯｜Root硬件密钥 |
| IMG-D01-G | 0001金质新工牌 |
| IMG-D02 | 旧机械键盘 |
| IMG-D03-A | 保温杯｜闭盖 |
| IMG-D03-B | 保温杯｜开盖枸杞 |
| IMG-D04-A | 防弹终端｜闭合 |
| IMG-D04-B | 防弹终端｜开启 |
| IMG-D05-A | 鱼竿｜伸展 |
| IMG-D05-B | 鱼竿｜收纳 |
| IMG-D06-A | 钓鱼水桶｜空桶 |
| IMG-D06-B | 钓鱼水桶｜一条海鲈鱼 |
| IMG-D07 | 露营灯 |
| IMG-D08-A | 协议文件夹｜未签 |
| IMG-D08-B | 协议文件夹｜签署后底板 |
| IMG-D09-A | 雨伞｜撑开 |
| IMG-D09-B | 雨伞｜收拢 |
| IMG-D10-A | 黑色轿车｜干燥 |
| IMG-D10-B | 黑色轿车｜雨夜 |
| IMG-D11-A | 主控物理终端｜待机 |
| IMG-D11-B | 主控物理终端｜接入 |
| IMG-D11-C | 主控物理终端｜恢复 |
| IMG-D12 | 贺凯智能表 |
| IMG-D13-BACK | 裴元手机｜背面 |
| IMG-D13-FRONT | 裴元手机｜正面 |
| IMG-S01-EMPTY-N | 总部监控大厅｜正常空景 |
| IMG-S01-R | 总部监控大厅｜崩盘红屏 |
| IMG-S01-G | 总部监控大厅｜恢复翠绿 |
| IMG-S01-CAM01 | 大厅｜踩工牌对峙底板 |
| IMG-S01-CAM02 | 大厅｜大屏铁证底板 |
| IMG-S01-CAM03 | 大厅｜北侧二层总裁看台 |
| IMG-S02-EMPTY-N | 地下核心机房｜正常空景 |
| IMG-S02-R | 机房｜故障空景 |
| IMG-S02-G | 机房｜恢复空景 |
| IMG-S02-CAM01 | 机房｜旧键盘操作底板 |
| IMG-S02-CAM02 | 机房｜键盘与密钥特写底板 |
| IMG-S03-EMPTY-D | 海边防波堤｜夜钓空景 |
| IMG-S03-W | 防波堤｜暴雨空景 |
| IMG-S03-CAM01 | 防波堤｜求救对峙底板 |
| IMG-S03-CAM02 | 防波堤｜跪递电脑底板 |
| IMG-S03-CAM03 | 防波堤｜沿湾远眺大厦 |
| IMG-S04-EMPTY-N | 大厦前场｜夜间空景 |
| IMG-S04-R | 大厦前场｜警报反射 |
| IMG-S04-M | 大厦前场｜晨光尾声 |
| IMG-S04-CAM01 | 大厦前场｜离场归来 |
| IMG-S05-EMPTY-W | 防波堤停车带｜暴雨空景 |
| IMG-S05-CAM01 | 停车带｜豪车长龙底板 |
| IMG-S06-EMPTY-N | 总部会客室｜空景 |
| IMG-S06-CAM01 | 会客室｜裴元视频背景 |
| IMG-S06-CAM02 | 会客室｜裴元欲逃 |
| IMG-FX01 | 雨丝层 |
| IMG-FX02 | 车灯光晕 |
| IMG-FX03 | 警报红光 |
| IMG-FX04 | 海边薄雾 |
| IMG-FX05 | 服务器火花 |
| IMG-FX06 | 盲敲残影备选素材 |

## IMG-STYLE01 · 真人影视风格定调

- 参考：无外部参考

用途／集数：全季摄影风格、色彩和材质方向

### 可复制提示词

> A 42-year-old Chinese man with a long rectangular face, a defined natural jaw, dark brown eyes, straight eyebrows with a small shallow notch at the outer end of his right eyebrow, short naturally side-parted black hair, a few gray hairs at both temples, fine lines at the eyes, clean-shaven, 182 cm tall, a tall lean balanced build with upright shoulders. Wearing thin rectangular dark gray metal eyeglasses. Wearing an open worn deep navy knee-length trench coat over a charcoal gray hoodie, straight indigo jeans, dark gray low-top casual shoes. Accessories: a dark-dial mechanical wristwatch on his left wrist. Standing calmly in a modern corporate monitoring hall at night, framed from the chest to just above the knees, arms relaxed. Dark metal surfaces, a large blank dark curved display, restrained cyan light strips and faint red alarm reflections in the background. Natural skin tones, a cool key light balanced with a subtle warm practical light. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 75 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P01-PORTRAIT · 周衍｜正面半身定脸

- 参考：无外部参考

用途／集数：先定脸；竖屏单人主图

### 可复制提示词

> A 42-year-old Chinese man with a long rectangular face, a defined natural jaw, dark brown eyes, straight eyebrows with a small shallow notch at the outer end of his right eyebrow, short naturally side-parted black hair, a few gray hairs at both temples, fine lines at the eyes, clean-shaven, 182 cm tall, a tall lean balanced build with upright shoulders. Wearing thin rectangular dark gray metal eyeglasses. Front-facing single-person chest-up casting portrait, head upright, neutral confident expression, shoulders visible. Wearing an open worn deep navy knee-length trench coat over a charcoal gray hoodie, straight indigo jeans, dark gray low-top casual shoes. Accessories: a dark-dial mechanical wristwatch on his left wrist. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P01-MASTER · 周衍｜三视图主卡

- 参考：无外部参考

用途／集数：身份与服装参考板；不作正片首帧

使用前：先附上已选P01-PORTRAIT人物图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 42-year-old Chinese man with a long rectangular face, a defined natural jaw, dark brown eyes, straight eyebrows with a small shallow notch at the outer end of his right eyebrow, short naturally side-parted black hair, a few gray hairs at both temples, fine lines at the eyes, clean-shaven, 182 cm tall, a tall lean balanced build with upright shoulders. Wearing thin rectangular dark gray metal eyeglasses. Wearing an open worn deep navy knee-length trench coat over a charcoal gray hoodie, straight indigo jeans, dark gray low-top casual shoes. Accessories: a dark-dial mechanical wristwatch on his left wrist. A photographic wardrobe continuity sheet with three evenly spaced full-body views of the same person, front view, left profile and back view in one horizontal row, identical scale and outfit in all views, relaxed standing poses, empty hands, full head and shoes visible. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 16:9 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P01-LOOK-A · 周衍｜基础服装全身

- 参考：无外部参考

用途／集数：E01及E03–04淋雨前

使用前：附上已选P01-PORTRAIT人物图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 42-year-old Chinese man with a long rectangular face, a defined natural jaw, dark brown eyes, straight eyebrows with a small shallow notch at the outer end of his right eyebrow, short naturally side-parted black hair, a few gray hairs at both temples, fine lines at the eyes, clean-shaven, 182 cm tall, a tall lean balanced build with upright shoulders. Wearing thin rectangular dark gray metal eyeglasses. Wearing an open worn deep navy knee-length trench coat over a charcoal gray hoodie, straight indigo jeans, dark gray low-top casual shoes. Accessories: a dark-dial mechanical wristwatch on his left wrist. Single-person full-length wardrobe photograph, relaxed standing pose, empty hands, complete head and both shoes inside the frame, dry clean clothing. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P01-EXPR-CALM · 周衍｜平静

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P01人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 42-year-old Chinese man with a long rectangular face, a defined natural jaw, dark brown eyes, straight eyebrows with a small shallow notch at the outer end of his right eyebrow, short naturally side-parted black hair, a few gray hairs at both temples, fine lines at the eyes, clean-shaven, 182 cm tall, a tall lean balanced build with upright shoulders. Wearing thin rectangular dark gray metal eyeglasses. Wearing an open worn deep navy knee-length trench coat over a charcoal gray hoodie, straight indigo jeans, dark gray low-top casual shoes. Accessories: a dark-dial mechanical wristwatch on his left wrist. One chest-up portrait of one person. Calm, focused eyes, naturally closed lips, head upright. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P01-EXPR-RESTRAINED · 周衍｜克制

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P01人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 42-year-old Chinese man with a long rectangular face, a defined natural jaw, dark brown eyes, straight eyebrows with a small shallow notch at the outer end of his right eyebrow, short naturally side-parted black hair, a few gray hairs at both temples, fine lines at the eyes, clean-shaven, 182 cm tall, a tall lean balanced build with upright shoulders. Wearing thin rectangular dark gray metal eyeglasses. Wearing an open worn deep navy knee-length trench coat over a charcoal gray hoodie, straight indigo jeans, dark gray low-top casual shoes. Accessories: a dark-dial mechanical wristwatch on his left wrist. One chest-up portrait of one person. Restrained irritation, gaze slightly down to the right, lips held firmly together. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P01-EXPR-FOCUSED · 周衍｜专注

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P01人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 42-year-old Chinese man with a long rectangular face, a defined natural jaw, dark brown eyes, straight eyebrows with a small shallow notch at the outer end of his right eyebrow, short naturally side-parted black hair, a few gray hairs at both temples, fine lines at the eyes, clean-shaven, 182 cm tall, a tall lean balanced build with upright shoulders. Wearing thin rectangular dark gray metal eyeglasses. Wearing an open worn deep navy knee-length trench coat over a charcoal gray hoodie, straight indigo jeans, dark gray low-top casual shoes. Accessories: a dark-dial mechanical wristwatch on his left wrist. One chest-up portrait of one person. Intensely focused, eyes slightly narrowed toward an off-camera monitor, closed mouth. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P01-EXPR-RELIEVED · 周衍｜释然

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P01人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 42-year-old Chinese man with a long rectangular face, a defined natural jaw, dark brown eyes, straight eyebrows with a small shallow notch at the outer end of his right eyebrow, short naturally side-parted black hair, a few gray hairs at both temples, fine lines at the eyes, clean-shaven, 182 cm tall, a tall lean balanced build with upright shoulders. Wearing thin rectangular dark gray metal eyeglasses. Wearing an open worn deep navy knee-length trench coat over a charcoal gray hoodie, straight indigo jeans, dark gray low-top casual shoes. Accessories: a dark-dial mechanical wristwatch on his left wrist. One chest-up portrait of one person. Quiet relief, relaxed eyes and a faint closed-mouth smile. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P02-PORTRAIT · 贺凯｜正面半身定脸

- 参考：无外部参考

用途／集数：先定脸；竖屏单人主图

### 可复制提示词

> A 32-year-old Chinese man with a narrow long face, slim dark brown eyes, thin lips, slick black hair parted on his left and combed back, clean-shaven, 178 cm tall, a lean build with defined shoulders. Wearing thin rectangular gold-rimmed eyeglasses. Front-facing single-person chest-up casting portrait, head upright, neutral confident expression, shoulders visible. Wearing a tailored deep blue three-piece suit, light gray dress shirt, dark navy tie, polished black leather shoes. Accessories: a black rectangular smartwatch on his right wrist. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P02-MASTER · 贺凯｜三视图主卡

- 参考：无外部参考

用途／集数：身份与服装参考板；不作正片首帧

使用前：先附上已选P02-PORTRAIT人物图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 32-year-old Chinese man with a narrow long face, slim dark brown eyes, thin lips, slick black hair parted on his left and combed back, clean-shaven, 178 cm tall, a lean build with defined shoulders. Wearing thin rectangular gold-rimmed eyeglasses. Wearing a tailored deep blue three-piece suit, light gray dress shirt, dark navy tie, polished black leather shoes. Accessories: a black rectangular smartwatch on his right wrist. A photographic wardrobe continuity sheet with three evenly spaced full-body views of the same person, front view, left profile and back view in one horizontal row, identical scale and outfit in all views, relaxed standing poses, empty hands, full head and shoes visible. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 16:9 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P02-LOOK-A · 贺凯｜基础服装全身

- 参考：无外部参考

用途／集数：E01–03淋雨前

使用前：附上已选P02-PORTRAIT人物图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 32-year-old Chinese man with a narrow long face, slim dark brown eyes, thin lips, slick black hair parted on his left and combed back, clean-shaven, 178 cm tall, a lean build with defined shoulders. Wearing thin rectangular gold-rimmed eyeglasses. Wearing a tailored deep blue three-piece suit, light gray dress shirt, dark navy tie, polished black leather shoes. Accessories: a black rectangular smartwatch on his right wrist. Single-person full-length wardrobe photograph, relaxed standing pose, empty hands, complete head and both shoes inside the frame, dry clean clothing. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P02-EXPR-CONTEMPT · 贺凯｜轻蔑

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P02人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 32-year-old Chinese man with a narrow long face, slim dark brown eyes, thin lips, slick black hair parted on his left and combed back, clean-shaven, 178 cm tall, a lean build with defined shoulders. Wearing thin rectangular gold-rimmed eyeglasses. Wearing a tailored deep blue three-piece suit, light gray dress shirt, dark navy tie, polished black leather shoes. Accessories: a black rectangular smartwatch on his right wrist. One chest-up portrait of one person. Contempt, one corner of the mouth slightly raised, gaze directed downward. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P02-EXPR-SHOCK · 贺凯｜错愕

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P02人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 32-year-old Chinese man with a narrow long face, slim dark brown eyes, thin lips, slick black hair parted on his left and combed back, clean-shaven, 178 cm tall, a lean build with defined shoulders. Wearing thin rectangular gold-rimmed eyeglasses. Wearing a tailored deep blue three-piece suit, light gray dress shirt, dark navy tie, polished black leather shoes. Accessories: a black rectangular smartwatch on his right wrist. One chest-up portrait of one person. Sudden shock, eyes widened naturally, lips slightly parted. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P02-EXPR-FEAR · 贺凯｜恐惧

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P02人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 32-year-old Chinese man with a narrow long face, slim dark brown eyes, thin lips, slick black hair parted on his left and combed back, clean-shaven, 178 cm tall, a lean build with defined shoulders. Wearing thin rectangular gold-rimmed eyeglasses. Wearing a tailored deep blue three-piece suit, light gray dress shirt, dark navy tie, polished black leather shoes. Accessories: a black rectangular smartwatch on his right wrist. One chest-up portrait of one person. Fear, tightened jaw and a fixed anxious gaze, rain-wet hair, gold-rimmed glasses slightly crooked. The original clothing has rain-darkened shoulders and damp hair. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P02-EXPR-RESENTMENT · 贺凯｜怨恨

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P02人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 32-year-old Chinese man with a narrow long face, slim dark brown eyes, thin lips, slick black hair parted on his left and combed back, clean-shaven, 178 cm tall, a lean build with defined shoulders. Wearing thin rectangular gold-rimmed eyeglasses. Wearing a tailored deep blue three-piece suit, light gray dress shirt, dark navy tie, polished black leather shoes. Accessories: a black rectangular smartwatch on his right wrist. One chest-up portrait of one person. Resentment, eyes shifted sideways, lips pressed shut, wet slick hair and crooked gold-rimmed glasses. The original clothing has rain-darkened shoulders and damp hair. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P03-PORTRAIT · 秦岚｜正面半身定脸

- 参考：无外部参考

用途／集数：先定脸；竖屏单人主图

### 可复制提示词

> A 28-year-old Chinese woman with an oval face, natural straight eyebrows, elongated almond-shaped dark brown eyes, a natural nose bridge, moderately full lips, subtle natural makeup, realistic skin texture, medium-length black hair tied in a low ponytail with a few loose strands at the temples, 170 cm tall, a naturally proportioned slender adult build. Front-facing single-person chest-up casting portrait, head upright, neutral confident expression, shoulders visible. Wearing a sharply tailored ivory white pantsuit with straight-leg trousers, a black high-neck knit top, black low-to-mid heel shoes. Accessories: small round diamond stud earrings. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P03-MASTER · 秦岚｜三视图主卡

- 参考：无外部参考

用途／集数：身份与服装参考板；不作正片首帧

使用前：先附上已选P03-PORTRAIT人物图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 28-year-old Chinese woman with an oval face, natural straight eyebrows, elongated almond-shaped dark brown eyes, a natural nose bridge, moderately full lips, subtle natural makeup, realistic skin texture, medium-length black hair tied in a low ponytail with a few loose strands at the temples, 170 cm tall, a naturally proportioned slender adult build. Wearing a sharply tailored ivory white pantsuit with straight-leg trousers, a black high-neck knit top, black low-to-mid heel shoes. Accessories: small round diamond stud earrings. A photographic wardrobe continuity sheet with three evenly spaced full-body views of the same person, front view, left profile and back view in one horizontal row, identical scale and outfit in all views, relaxed standing poses, empty hands, full head and shoes visible. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 16:9 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P03-LOOK-A · 秦岚｜基础服装全身

- 参考：无外部参考

用途／集数：E01–03到海边前

使用前：附上已选P03-PORTRAIT人物图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 28-year-old Chinese woman with an oval face, natural straight eyebrows, elongated almond-shaped dark brown eyes, a natural nose bridge, moderately full lips, subtle natural makeup, realistic skin texture, medium-length black hair tied in a low ponytail with a few loose strands at the temples, 170 cm tall, a naturally proportioned slender adult build. Wearing a sharply tailored ivory white pantsuit with straight-leg trousers, a black high-neck knit top, black low-to-mid heel shoes. Accessories: small round diamond stud earrings. Single-person full-length wardrobe photograph, relaxed standing pose, empty hands, complete head and both shoes inside the frame, dry clean clothing. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P03-EXPR-ASSESSING · 秦岚｜审视

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P03人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 28-year-old Chinese woman with an oval face, natural straight eyebrows, elongated almond-shaped dark brown eyes, a natural nose bridge, moderately full lips, subtle natural makeup, realistic skin texture, medium-length black hair tied in a low ponytail with a few loose strands at the temples, 170 cm tall, a naturally proportioned slender adult build. Wearing a sharply tailored ivory white pantsuit with straight-leg trousers, a black high-neck knit top, black low-to-mid heel shoes. Accessories: small round diamond stud earrings. One chest-up portrait of one person. Assessing, steady direct gaze, closed lips. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P03-EXPR-SHOCK · 秦岚｜震惊

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P03人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 28-year-old Chinese woman with an oval face, natural straight eyebrows, elongated almond-shaped dark brown eyes, a natural nose bridge, moderately full lips, subtle natural makeup, realistic skin texture, medium-length black hair tied in a low ponytail with a few loose strands at the temples, 170 cm tall, a naturally proportioned slender adult build. Wearing a sharply tailored ivory white pantsuit with straight-leg trousers, a black high-neck knit top, black low-to-mid heel shoes. Accessories: small round diamond stud earrings. One chest-up portrait of one person. Shocked, slightly drawn brows, eyes widened naturally, lips parted. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P03-EXPR-PLEADING · 秦岚｜恳切

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P03人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 28-year-old Chinese woman with an oval face, natural straight eyebrows, elongated almond-shaped dark brown eyes, a natural nose bridge, moderately full lips, subtle natural makeup, realistic skin texture, medium-length black hair tied in a low ponytail with a few loose strands at the temples, 170 cm tall, a naturally proportioned slender adult build. Wearing a sharply tailored ivory white pantsuit with straight-leg trousers, a black high-neck knit top, black low-to-mid heel shoes. Accessories: small round diamond stud earrings. One chest-up portrait of one person. Sincere and pleading, gaze lifted slightly, faint redness at the eyes, damp strands against her cheeks. The original clothing has rain-darkened shoulders and damp hair. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P03-EXPR-RESOLUTE · 秦岚｜坚定

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P03人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 28-year-old Chinese woman with an oval face, natural straight eyebrows, elongated almond-shaped dark brown eyes, a natural nose bridge, moderately full lips, subtle natural makeup, realistic skin texture, medium-length black hair tied in a low ponytail with a few loose strands at the temples, 170 cm tall, a naturally proportioned slender adult build. Wearing a sharply tailored ivory white pantsuit with straight-leg trousers, a black high-neck knit top, black low-to-mid heel shoes. Accessories: small round diamond stud earrings. One chest-up portrait of one person. Resolute, steady jaw and direct gaze, closed lips, damp hair strands. The original clothing has rain-darkened shoulders and damp hair. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P04-PORTRAIT · 唐小川｜正面半身定脸

- 参考：无外部参考

用途／集数：先定脸；竖屏单人主图

### 可复制提示词

> A 25-year-old Chinese man with a rounded square face, naturally thick eyebrows, dark brown eyes, short tousled black hair, clean-shaven, 175 cm tall, an ordinary balanced adult build. Wearing black square-frame eyeglasses. Front-facing single-person chest-up casting portrait, head upright, neutral confident expression, shoulders visible. Wearing a blue-gray shirt with fine dark red checks over a black crew-neck T-shirt, dark gray work trousers, white and gray sneakers. Accessories: a blue-gray lanyard holding a blank employee badge. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P04-MASTER · 唐小川｜三视图主卡

- 参考：无外部参考

用途／集数：身份与服装参考板；不作正片首帧

使用前：先附上已选P04-PORTRAIT人物图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 25-year-old Chinese man with a rounded square face, naturally thick eyebrows, dark brown eyes, short tousled black hair, clean-shaven, 175 cm tall, an ordinary balanced adult build. Wearing black square-frame eyeglasses. Wearing a blue-gray shirt with fine dark red checks over a black crew-neck T-shirt, dark gray work trousers, white and gray sneakers. Accessories: a blue-gray lanyard holding a blank employee badge. A photographic wardrobe continuity sheet with three evenly spaced full-body views of the same person, front view, left profile and back view in one horizontal row, identical scale and outfit in all views, relaxed standing poses, empty hands, full head and shoes visible. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 16:9 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P04-LOOK-A · 唐小川｜基础服装全身

- 参考：无外部参考

用途／集数：E01–04

使用前：附上已选P04-PORTRAIT人物图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 25-year-old Chinese man with a rounded square face, naturally thick eyebrows, dark brown eyes, short tousled black hair, clean-shaven, 175 cm tall, an ordinary balanced adult build. Wearing black square-frame eyeglasses. Wearing a blue-gray shirt with fine dark red checks over a black crew-neck T-shirt, dark gray work trousers, white and gray sneakers. Accessories: a blue-gray lanyard holding a blank employee badge. Single-person full-length wardrobe photograph, relaxed standing pose, empty hands, complete head and both shoes inside the frame, dry clean clothing. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P04-EXPR-INDIGNANT · 唐小川｜不平

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P04人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 25-year-old Chinese man with a rounded square face, naturally thick eyebrows, dark brown eyes, short tousled black hair, clean-shaven, 175 cm tall, an ordinary balanced adult build. Wearing black square-frame eyeglasses. Wearing a blue-gray shirt with fine dark red checks over a black crew-neck T-shirt, dark gray work trousers, white and gray sneakers. Accessories: a blue-gray lanyard holding a blank employee badge. One chest-up portrait of one person. Indignant, brows drawn together slightly, lips pressed tight. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P04-EXPR-ANXIOUS · 唐小川｜焦急

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P04人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 25-year-old Chinese man with a rounded square face, naturally thick eyebrows, dark brown eyes, short tousled black hair, clean-shaven, 175 cm tall, an ordinary balanced adult build. Wearing black square-frame eyeglasses. Wearing a blue-gray shirt with fine dark red checks over a black crew-neck T-shirt, dark gray work trousers, white and gray sneakers. Accessories: a blue-gray lanyard holding a blank employee badge. One chest-up portrait of one person. Anxious, gaze toward the left, lips slightly parted. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P04-EXPR-CERTAIN · 唐小川｜确信

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P04人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 25-year-old Chinese man with a rounded square face, naturally thick eyebrows, dark brown eyes, short tousled black hair, clean-shaven, 175 cm tall, an ordinary balanced adult build. Wearing black square-frame eyeglasses. Wearing a blue-gray shirt with fine dark red checks over a black crew-neck T-shirt, dark gray work trousers, white and gray sneakers. Accessories: a blue-gray lanyard holding a blank employee badge. One chest-up portrait of one person. Certain and confident, steady eyes, head upright, closed mouth. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P04-EXPR-HAPPY · 唐小川｜欣喜

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P04人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 25-year-old Chinese man with a rounded square face, naturally thick eyebrows, dark brown eyes, short tousled black hair, clean-shaven, 175 cm tall, an ordinary balanced adult build. Wearing black square-frame eyeglasses. Wearing a blue-gray shirt with fine dark red checks over a black crew-neck T-shirt, dark gray work trousers, white and gray sneakers. Accessories: a blue-gray lanyard holding a blank employee badge. One chest-up portrait of one person. Relieved happiness, relaxed eyes and a natural small smile. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P05-PORTRAIT · 魏哲｜正面半身定脸

- 参考：无外部参考

用途／集数：先定脸；竖屏单人主图

### 可复制提示词

> A 48-year-old Chinese man with a broad forehead, a slightly square jaw, fine under-eye lines, short black-and-gray hair combed back, distinct gray hair at both sides, dark brown eyes, clean-shaven, 176 cm tall, a medium adult build. Wearing thin silver-gray metal eyeglasses. Front-facing single-person chest-up casting portrait, head upright, neutral confident expression, shoulders visible. Wearing a dark gray cashmere suit, off-white shirt, burgundy tie, black leather shoes.  Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P05-MASTER · 魏哲｜三视图主卡

- 参考：无外部参考

用途／集数：身份与服装参考板；不作正片首帧

使用前：先附上已选P05-PORTRAIT人物图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 48-year-old Chinese man with a broad forehead, a slightly square jaw, fine under-eye lines, short black-and-gray hair combed back, distinct gray hair at both sides, dark brown eyes, clean-shaven, 176 cm tall, a medium adult build. Wearing thin silver-gray metal eyeglasses. Wearing a dark gray cashmere suit, off-white shirt, burgundy tie, black leather shoes.  A photographic wardrobe continuity sheet with three evenly spaced full-body views of the same person, front view, left profile and back view in one horizontal row, identical scale and outfit in all views, relaxed standing poses, empty hands, full head and shoes visible. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 16:9 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P05-LOOK-A · 魏哲｜基础服装全身

- 参考：无外部参考

用途／集数：E02入场

使用前：附上已选P05-PORTRAIT人物图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 48-year-old Chinese man with a broad forehead, a slightly square jaw, fine under-eye lines, short black-and-gray hair combed back, distinct gray hair at both sides, dark brown eyes, clean-shaven, 176 cm tall, a medium adult build. Wearing thin silver-gray metal eyeglasses. Wearing a dark gray cashmere suit, off-white shirt, burgundy tie, black leather shoes.  Single-person full-length wardrobe photograph, relaxed standing pose, empty hands, complete head and both shoes inside the frame, dry clean clothing. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P05-EXPR-ARROGANT · 魏哲｜倨傲

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P05人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 48-year-old Chinese man with a broad forehead, a slightly square jaw, fine under-eye lines, short black-and-gray hair combed back, distinct gray hair at both sides, dark brown eyes, clean-shaven, 176 cm tall, a medium adult build. Wearing thin silver-gray metal eyeglasses. Wearing a dark gray cashmere suit, off-white shirt, burgundy tie, black leather shoes.  One chest-up portrait of one person. Arrogant, chin slightly raised, eyes looking down, lips closed. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P05-EXPR-FLUSTERED · 魏哲｜失措

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P05人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 48-year-old Chinese man with a broad forehead, a slightly square jaw, fine under-eye lines, short black-and-gray hair combed back, distinct gray hair at both sides, dark brown eyes, clean-shaven, 176 cm tall, a medium adult build. Wearing thin silver-gray metal eyeglasses. Wearing a dark gray cashmere suit, off-white shirt, burgundy tie, black leather shoes.  One chest-up portrait of one person. Flustered, a natural sheen of sweat on the forehead, eyes fixed on an off-camera monitor, lips parted. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P05-EXPR-AWESTRUCK · 魏哲｜震撼

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P05人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 48-year-old Chinese man with a broad forehead, a slightly square jaw, fine under-eye lines, short black-and-gray hair combed back, distinct gray hair at both sides, dark brown eyes, clean-shaven, 176 cm tall, a medium adult build. Wearing thin silver-gray metal eyeglasses. Wearing a dark gray cashmere suit, off-white shirt, burgundy tie, black leather shoes.  One chest-up portrait of one person. Awestruck, raised eyebrows, sharply focused eyes, rain-damp hair. The original clothing has rain-darkened shoulders and damp hair. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P05-EXPR-FRIGHTENED · 魏哲｜惊惧

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P05人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 48-year-old Chinese man with a broad forehead, a slightly square jaw, fine under-eye lines, short black-and-gray hair combed back, distinct gray hair at both sides, dark brown eyes, clean-shaven, 176 cm tall, a medium adult build. Wearing thin silver-gray metal eyeglasses. Wearing a dark gray cashmere suit, off-white shirt, burgundy tie, black leather shoes.  One chest-up portrait of one person. Frightened, tense brows, slightly trembling lips, eyes lifted toward a taller man outside the frame. The original clothing has rain-darkened shoulders and damp hair. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P06-PORTRAIT · 裴元｜正面半身定脸

- 参考：无外部参考

用途／集数：先定脸；竖屏单人主图

### 可复制提示词

> A 50-year-old Chinese man with a narrow angular jaw, dark brown eyes, neatly slicked-back black-and-gray hair, a small faint mole below his left eye, fine lines at the corners of the eyes, clean-shaven, 180 cm tall, an upright well-proportioned adult build. Front-facing single-person chest-up casting portrait, head upright, neutral confident expression, shoulders visible. Wearing a black double-breasted overcoat over a charcoal suit, white shirt, dark gray tie, black leather shoes. Accessories: a plain platinum cufflink visible at his left shirt cuff. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P06-MASTER · 裴元｜三视图主卡

- 参考：无外部参考

用途／集数：身份与服装参考板；不作正片首帧

使用前：先附上已选P06-PORTRAIT人物图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 50-year-old Chinese man with a narrow angular jaw, dark brown eyes, neatly slicked-back black-and-gray hair, a small faint mole below his left eye, fine lines at the corners of the eyes, clean-shaven, 180 cm tall, an upright well-proportioned adult build. Wearing a black double-breasted overcoat over a charcoal suit, white shirt, dark gray tie, black leather shoes. Accessories: a plain platinum cufflink visible at his left shirt cuff. A photographic wardrobe continuity sheet with three evenly spaced full-body views of the same person, front view, left profile and back view in one horizontal row, identical scale and outfit in all views, relaxed standing poses, empty hands, full head and shoes visible. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 16:9 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P06-LOOK-A · 裴元｜基础服装全身

- 参考：无外部参考

用途／集数：E03–06

使用前：附上已选P06-PORTRAIT人物图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 50-year-old Chinese man with a narrow angular jaw, dark brown eyes, neatly slicked-back black-and-gray hair, a small faint mole below his left eye, fine lines at the corners of the eyes, clean-shaven, 180 cm tall, an upright well-proportioned adult build. Wearing a black double-breasted overcoat over a charcoal suit, white shirt, dark gray tie, black leather shoes. Accessories: a plain platinum cufflink visible at his left shirt cuff. Single-person full-length wardrobe photograph, relaxed standing pose, empty hands, complete head and both shoes inside the frame, dry clean clothing. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P06-EXPR-COLD · 裴元｜冷漠

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P06人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 50-year-old Chinese man with a narrow angular jaw, dark brown eyes, neatly slicked-back black-and-gray hair, a small faint mole below his left eye, fine lines at the corners of the eyes, clean-shaven, 180 cm tall, an upright well-proportioned adult build. Wearing a black double-breasted overcoat over a charcoal suit, white shirt, dark gray tie, black leather shoes. Accessories: a plain platinum cufflink visible at his left shirt cuff. One chest-up portrait of one person. Cold, level gaze and closed lips. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P06-EXPR-CONFIDENT · 裴元｜笃定

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P06人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 50-year-old Chinese man with a narrow angular jaw, dark brown eyes, neatly slicked-back black-and-gray hair, a small faint mole below his left eye, fine lines at the corners of the eyes, clean-shaven, 180 cm tall, an upright well-proportioned adult build. Wearing a black double-breasted overcoat over a charcoal suit, white shirt, dark gray tie, black leather shoes. Accessories: a plain platinum cufflink visible at his left shirt cuff. One chest-up portrait of one person. Confident, a barely visible smile and steady calculating eyes. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P06-EXPR-ALERT · 裴元｜警觉

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P06人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 50-year-old Chinese man with a narrow angular jaw, dark brown eyes, neatly slicked-back black-and-gray hair, a small faint mole below his left eye, fine lines at the corners of the eyes, clean-shaven, 180 cm tall, an upright well-proportioned adult build. Wearing a black double-breasted overcoat over a charcoal suit, white shirt, dark gray tie, black leather shoes. Accessories: a plain platinum cufflink visible at his left shirt cuff. One chest-up portrait of one person. Alert, eyes shifted to the right, lips tightened. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P06-EXPR-FROZEN · 裴元｜僵硬

- 参考：无外部参考

用途／集数：单张表情参考，非四宫格

使用前：附上已选P06人物主图；雨后表情选对应湿衣图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 50-year-old Chinese man with a narrow angular jaw, dark brown eyes, neatly slicked-back black-and-gray hair, a small faint mole below his left eye, fine lines at the corners of the eyes, clean-shaven, 180 cm tall, an upright well-proportioned adult build. Wearing a black double-breasted overcoat over a charcoal suit, white shirt, dark gray tie, black leather shoes. Accessories: a plain platinum cufflink visible at his left shirt cuff. One chest-up portrait of one person. Frozen disbelief, all trace of the earlier smile gone, subtle facial tension. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P01-A-W · 周衍｜湿风衣

- 参考：无外部参考

用途／集数：E03海边淋雨后–E05入机房

使用前：附上已选P01人物主图，并按需要附原服装图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 42-year-old Chinese man with a long rectangular face, a defined natural jaw, dark brown eyes, straight eyebrows with a small shallow notch at the outer end of his right eyebrow, short naturally side-parted black hair, a few gray hairs at both temples, fine lines at the eyes, clean-shaven, 182 cm tall, a tall lean balanced build with upright shoulders. Wearing thin rectangular dark gray metal eyeglasses. The original deep navy trench coat is rain-soaked at the shoulders, cuffs and hem with darker wet patches. The charcoal hoodie is slightly damp at the shoulders, jean hems and shoes are wet, hair tips wet, glasses straight. Single full-length standing pose, empty hands, calm. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P01-LOOK-B · 周衍｜脱风衣挽袖

- 参考：无外部参考

用途／集数：E05–06

使用前：附上已选P01人物主图，并按需要附原服装图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 42-year-old Chinese man with a long rectangular face, a defined natural jaw, dark brown eyes, straight eyebrows with a small shallow notch at the outer end of his right eyebrow, short naturally side-parted black hair, a few gray hairs at both temples, fine lines at the eyes, clean-shaven, 182 cm tall, a tall lean balanced build with upright shoulders. Wearing thin rectangular dark gray metal eyeglasses. The trench coat is absent. Wearing only the charcoal gray hoodie, straight indigo jeans and dark gray casual shoes. Both sleeves pushed evenly to the middle of the forearms, dark-dial mechanical watch visible on the left wrist. Faint damp patches at the hoodie collar and shoulders, wet trouser hems and shoes. Glasses worn normally, empty hands, focused full-length standing pose. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P01-B-N · 周衍｜摘镜闭眼

- 参考：无外部参考

用途／集数：E05最后10秒–E06恢复操作

使用前：附上已选P01人物主图，并按需要附原服装图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 42-year-old Chinese man with a long rectangular face, a defined natural jaw, dark brown eyes, straight eyebrows with a small shallow notch at the outer end of his right eyebrow, short naturally side-parted black hair, a few gray hairs at both temples, fine lines at the eyes, clean-shaven, 182 cm tall, a tall lean balanced build with upright shoulders. Chest-up portrait, trench coat absent, charcoal hoodie sleeves pushed to mid-forearm. Eyeglasses removed and absent from the face, eyes gently closed, a faint cool confident smile, realistic eyelids and skin pores. Slight damp color variation at the shoulders, empty frame below the chest, a steady still pose. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P02-A-W · 贺凯｜下跪前湿西装

- 参考：无外部参考

用途／集数：E03末–E04下跪前

使用前：附上已选P02人物主图，并按需要附原服装图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 32-year-old Chinese man with a narrow long face, slim dark brown eyes, thin lips, slick black hair parted on his left and combed back, clean-shaven, 178 cm tall, a lean build with defined shoulders. Wearing thin rectangular gold-rimmed eyeglasses. The original deep blue three-piece suit is rain-soaked, darker patches on the chest and shoulders, wet trouser hems, damp shirt collar, wet hair still parted on his left. Glasses straight, black smartwatch on the right wrist. Knees still clean, empty hands, tense full-length standing pose. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P02-LOOK-B · 贺凯｜泥膝狼狈态

- 参考：无外部参考

用途／集数：E04跪下后–E06

使用前：附上已选P02人物主图，并按需要附原服装图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 32-year-old Chinese man with a narrow long face, slim dark brown eyes, thin lips, slick black hair parted on his left and combed back, clean-shaven, 178 cm tall, a lean build with defined shoulders. Wearing thin rectangular gold-rimmed eyeglasses. The original deep blue three-piece suit is soaked. Fixed gray-brown mud stains on both knees, the left knee stain slightly larger, muddy wet hems and shoes. Navy tie tilted to his left, gold-rimmed glasses slightly crooked, wet hair stuck near the forehead, black smartwatch on the right wrist. Empty hands, terrified full-length standing pose. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P03-A-W · 秦岚｜雨后白西装

- 参考：无外部参考

用途／集数：E03末–E06

使用前：附上已选P03人物主图，并按需要附原服装图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 28-year-old Chinese woman with an oval face, natural straight eyebrows, elongated almond-shaped dark brown eyes, a natural nose bridge, moderately full lips, subtle natural makeup, realistic skin texture, medium-length black hair tied in a low ponytail with a few loose strands at the temples, 170 cm tall, a naturally proportioned slender adult build. The original ivory white pantsuit has damp shoulders, cuffs and trouser hems, slightly darkened yet fully opaque heavy fabric. Black high-neck top unchanged. Low ponytail tips wet, two loose strands damp against her cheeks, diamond studs unchanged. Black low-to-mid heel shoes wet, knees clean, empty hands, upright full-length standing pose. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P04-A-L · 唐小川｜值守疲惫

- 参考：无外部参考

用途／集数：E05–06，始终留守总部

使用前：附上已选P04人物主图，并按需要附原服装图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 25-year-old Chinese man with a rounded square face, naturally thick eyebrows, dark brown eyes, short tousled black hair, clean-shaven, 175 cm tall, an ordinary balanced adult build. Wearing black square-frame eyeglasses. The original blue-gray dark-red-check shirt has both sleeves rolled to mid-forearm, slightly creased hem. Black square glasses and blue-gray employee lanyard unchanged, mild under-eye fatigue. Clothing dry and clean, empty hands, alert full-length standing pose. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P05-A-S · 魏哲｜专家失利

- 参考：无外部参考

用途／集数：E02失利后–E03

使用前：附上已选P05人物主图，并按需要附原服装图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 48-year-old Chinese man with a broad forehead, a slightly square jaw, fine under-eye lines, short black-and-gray hair combed back, distinct gray hair at both sides, dark brown eyes, clean-shaven, 176 cm tall, a medium adult build. Wearing thin silver-gray metal eyeglasses. The original dark gray cashmere suit is dry but slightly creased at the front. One top shirt button open, burgundy tie knot slightly lowered, natural sweat sheen on the forehead, silver-gray glasses unchanged. Empty hands, flustered full-length standing pose. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P05-A-W · 魏哲｜雨后狼狈

- 参考：无外部参考

用途／集数：E04–06

使用前：附上已选P05人物主图，并按需要附原服装图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 48-year-old Chinese man with a broad forehead, a slightly square jaw, fine under-eye lines, short black-and-gray hair combed back, distinct gray hair at both sides, dark brown eyes, clean-shaven, 176 cm tall, a medium adult build. Wearing thin silver-gray metal eyeglasses. The original dark gray cashmere suit has wet shoulders and trouser hems. Top shirt button open, burgundy tie knot slightly lowered, hair tips damp, gray temples and silver-gray glasses unchanged. Knees clean, empty hands, exhausted full-length standing pose. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P02-KNEEL · 贺凯｜跪递防弹电脑

- 参考：无外部参考

用途／集数：E04，踢膝后已跪稳的终态

使用前：附上已选P02湿衣泥膝图与D04-B电脑图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 32-year-old Chinese man with a narrow long face, slim dark brown eyes, thin lips, slick black hair parted on his left and combed back, clean-shaven, 178 cm tall, a lean build with defined shoulders. Wearing thin rectangular gold-rimmed eyeglasses. Wearing the original rain-soaked deep blue three-piece suit, muddy knees, crooked gold-rimmed glasses and right-wrist black smartwatch. Both knees on the ground, back leaning slightly forward, both hands supporting the underside of one open rugged black-gray 14-inch laptop and raising it toward a person outside the frame in front of him. The laptop screen faces that off-camera person, back of the display toward the kneeling man, blank dark display. Humiliated and frightened, one person and one laptop, stable final kneeling pose. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-P05-KNEEL · 魏哲｜认出Zero后跪拜

- 参考：无外部参考

用途／集数：E05认出周衍身份后

使用前：附上已选P05人物主图与P05-A-W状态图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A 48-year-old Chinese man with a broad forehead, a slightly square jaw, fine under-eye lines, short black-and-gray hair combed back, distinct gray hair at both sides, dark brown eyes, clean-shaven, 176 cm tall, a medium adult build. Wearing thin silver-gray metal eyeglasses. Wearing the original wet dark gray cashmere suit, off-white shirt and loosened burgundy tie. Both knees on the floor, back stiff, head slightly lifted toward someone above and outside the frame, hands empty beside his thighs, shocked recognition. One person, a stable kneeling pose, realistic knees and body proportions. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-G01 · 值守员工

- 参考：无外部参考

用途／集数：E01–02、E05–06

### 可复制提示词

> One Chinese adult engineer aged 25 to 45, ordinary build, dark gray or navy everyday business clothes, blank employee badge, full-length neutral standing pose. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-G02 · 随行人员

- 参考：无外部参考

用途／集数：E03–04

### 可复制提示词

> One Chinese adult corporate driver or administrative assistant, dark rainproof jacket and trousers, ordinary build, full-length neutral standing pose. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-G03 · 法务／便衣警方群演

- 参考：无外部参考

用途／集数：E06带走反派

### 可复制提示词

> One Chinese adult plainclothes investigator or legal staff member, ordinary dark jacket and trousers, professional neutral bearing, empty hands, full-length standing pose. Seamless light gray studio background, soft even studio lighting, natural skin tones, clear facial details. Photorealistic live-action photography, contemporary Chinese urban drama, natural skin texture, realistic age and anatomy, authentic fabric and materials, restrained cinematic color grading. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D01-A · 0001工牌｜完整

- 参考：无外部参考

用途／集数：E01

### 可复制提示词

> One horizontal employee ID badge, 86 by 54 mm, frosted gray-blue plastic case, a small blank portrait area on the left and blank number area on the right, blue-gray fabric lanyard attached at the top. Intact exterior with the internal titanium token concealed. Centered single object, 45-degree overhead view. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 1:1 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D01-B · 0001工牌｜裂壳

- 参考：无外部参考

用途／集数：E01踩裂后

使用前：附上同编号已选主卡，保持外壳、磨痕和接口。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> One horizontal gray-blue employee ID badge matching the original case, a main diagonal crack from upper right to lower left across the plastic front, a few small fragments still attached at the lower corner, titanium core intact and unbent, blue-gray lanyard attached. Resting flat, 45-degree overhead view, one damaged badge, empty surrounding surface. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 1:1 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D01-C · 0001内芯｜Root硬件密钥

- 参考：无外部参考

用途／集数：E01周衍捡走，E05–06接入

使用前：附上同编号已选主卡，保持外壳、磨痕和接口。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> One small rectangular titanium hardware root token, 32 by 18 by 3 mm, rounded corners, fine old scratches, one narrow row of contact pads at a short edge, two tiny screws on the back, a small blank number area on the front. A solid non-glowing practical prop, 45-degree overhead view, one token. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 1:1 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D01-G · 0001金质新工牌

- 参考：无外部参考

用途／集数：E06秦岚奉还

使用前：附上同编号已选主卡，保持外壳、磨痕和接口。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> One new matte pale-gold employee ID badge, 86 by 54 mm, rounded corners, blank number area, blue-gray lanyard. A solid ceremonial badge with a closed plain body, visually separate from the small titanium root token. Centered single object, 45-degree overhead view. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 1:1 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D02 · 旧机械键盘

- 参考：无外部参考

用途／集数：E01交徒弟；E05–06使用

### 可复制提示词

> One compact 87-key mechanical keyboard, charcoal gray plastic housing, gray-white keycaps with blank tops, orderly key layout, subtle polished wear from years of use, a distinct worn patch at the center of the spacebar, a small pale scratch at the upper right corner. One black cable exits from the rear right and continues out of frame, unlit keys, 45-degree overhead view. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 1:1 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D03-A · 保温杯｜闭盖

- 参考：无外部参考

用途／集数：E01、03–04

### 可复制提示词

> One 500 ml matte graphite gray stainless steel vacuum flask, 23 cm tall and about 7 cm wide, simple cylindrical body, short screw-on lid closed, narrow rubber ring at the base, one faint vertical use scratch. Plain handle-free body, single centered object, 45-degree overhead view. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 1:1 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D03-B · 保温杯｜开盖枸杞

- 参考：无外部参考

用途／集数：E04

使用前：附上同编号已选主卡，保持外壳、磨痕和接口。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> One matte graphite gray cylindrical 500 ml vacuum flask matching the closed version, screw lid removed and placed to the right, a little soft steam at the opening, dark tea with two or three faint red goji berries visible inside. The same single body scratch, 45-degree overhead view. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 1:1 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D04-A · 防弹终端｜闭合

- 参考：无外部参考

用途／集数：E03–04

### 可复制提示词

> One closed rugged black-gray 14-inch laptop used as a movie prop, thick rounded protective corner bumpers, one latch on the front edge, continuous hinge at the back, a covered waterproof connector on the left side, fine anti-slip shell texture, approximately 34 by 26 by 4 cm. Centered single object, 45-degree overhead view. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 16:9 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D04-B · 防弹终端｜开启

- 参考：无外部参考

用途／集数：E04–05跪递与按键

使用前：附上同编号已选主卡，保持外壳、磨痕和接口。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> One rugged black-gray 14-inch laptop matching the closed prop, lid open about 110 degrees, hinge at the rear, keyboard facing the viewer, thick protective corners, one covered left-side connector. The upper display and lower keyboard are clearly separate planes, dark blank screen and blank keycaps, front three-quarter view. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 16:9 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D05-A · 鱼竿｜伸展

- 参考：无外部参考

用途／集数：E03–04

### 可复制提示词

> One fully extended 2.1-meter black-gray sea-fishing rod, complete side profile, grip at the right end with a silver-gray spinning reel attached underneath, rod tip pointing left, fine fishing line threaded neatly through the guide rings. One complete rod, isolated object. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 16:9 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D05-B · 鱼竿｜收纳

- 参考：无外部参考

用途／集数：E06背起离开

使用前：附上同编号已选主卡，保持外壳、磨痕和接口。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> One black-gray fishing rod broken down into a neat approximately 70 cm bundle, the same silver-gray spinning reel attached to the original grip section, dark gray fabric straps holding the sections together. One compact bundle, side profile. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 16:9 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D06-A · 钓鱼水桶｜空桶

- 参考：无外部参考

用途／集数：E03

### 可复制提示词

> One dark gray 20-liter plastic fishing bucket, about 35 cm tall and 30 cm across, a single folding semicircular handle, slight saltwater marks on the outside, a little clear water inside the otherwise empty bucket. 45-degree overhead view. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 1:1 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D06-B · 钓鱼水桶｜一条海鲈鱼

- 参考：无外部参考

用途／集数：E03–04

使用前：附上同编号已选主卡，保持外壳、磨痕和接口。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> One dark gray 20-liter fishing bucket with a single folding handle and slight saltwater wear, shallow water inside containing exactly one intact silver-gray sea bass about 30 cm long, natural uninjured fish. 45-degree overhead view. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 1:1 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D07 · 露营灯

- 参考：无外部参考

用途／集数：E03–04钓位

### 可复制提示词

> One portable camping lantern about 24 cm tall, black circular base, translucent milky cylindrical shade, black round top with an arched carrying handle, evenly glowing low-intensity warm amber light, clear lamp silhouette with controlled bloom. Single centered object. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 1:1 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D08-A · 协议文件夹｜未签

- 参考：无外部参考

用途／集数：E04签字前

### 可复制提示词

> One open black hard-cover A4 document folder lying flat, a central metal clip holding two ivory sheets of blank paper, generous empty signature area near the bottom of the top sheet, one dark gray metal pen beside the folder with its cap on the back. 45-degree overhead view. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 1:1 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D08-B · 协议文件夹｜签署后底板

- 参考：无外部参考

用途／集数：E04签字后–E06

使用前：附上同编号已选主卡，保持外壳、磨痕和接口。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> One open black hard-cover A4 folder matching the earlier prop, two ivory sheets held by the same metal clip, blank surface reserved for a signature composited later, one dark gray pen resting horizontally along the bottom edge. 45-degree overhead view, unchanged folder geometry. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 1:1 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D09-A · 雨伞｜撑开

- 参考：无外部参考

用途／集数：E03–04

### 可复制提示词

> One fully opened black long-handled umbrella, eight ribs, straight silver-gray shaft, curved black handle, canopy about 105 cm wide, shaft vertical, three-quarter side view, a few realistic water droplets. Complete single object. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 9:16 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D09-B · 雨伞｜收拢

- 参考：无外部参考

用途／集数：E03–04变体

使用前：附上同编号已选主卡，保持外壳、磨痕和接口。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> One closed black long-handled umbrella, silver-gray straight shaft, curved black handle, black fastening strap secured around the folded canopy, intact neatly folded ribs, a few water droplets, full object visible. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 9:16 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D10-A · 黑色轿车｜干燥

- 参考：无外部参考

用途／集数：车体主卡

### 可复制提示词

> One unbranded black four-door executive sedan about 5 meters long, left-hand drive, black five-spoke wheels, narrow horizontal headlamps, blank dark gray license plate, dry bodywork, front-left three-quarter view, all doors closed, empty interior. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 16:9 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D10-B · 黑色轿车｜雨夜

- 参考：无外部参考

用途／集数：E03–05车队

使用前：附上同编号已选主卡，保持外壳、磨痕和接口。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> One unbranded black four-door executive sedan matching the master design, left-hand drive, black five-spoke wheels and narrow headlamps unchanged. Rain beads on the body, a little wet mud at the tires and lower sills, headlights on with controlled exposure, all doors closed, empty interior, blank plate, front-left three-quarter view. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 16:9 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D11-A · 主控物理终端｜待机

- 参考：无外部参考

用途／集数：E02、05

### 可复制提示词

> One fixed black metal server maintenance workstation, 140 cm wide, 70 cm deep and 90 cm high. A 24-inch screen set into the desktop tilted slightly back, a small covered hardware recovery slot at the lower right of the front face, a separate wired keyboard input port on the right side of the desktop, enclosed cable tray beneath. Empty keyboard space, blank dark screen, front three-quarter view. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 16:9 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D11-B · 主控物理终端｜接入

- 参考：无外部参考

用途／集数：E05–06

使用前：附上同编号已选主卡，保持外壳、磨痕和接口。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> One black metal server maintenance workstation matching the master design, 140 by 70 by 90 cm. Recovery cover open at the lower right front, one small titanium root token inserted with a short end exposed. One charcoal 87-key keyboard with gray-white blank keycaps on the desktop, a single cable from its rear right connected to the right-side keyboard port. Blank dark gray screen, front three-quarter view. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 16:9 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D11-C · 主控物理终端｜恢复

- 参考：无外部参考

用途／集数：E06

使用前：附上同编号已选主卡，保持外壳、磨痕和接口。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> One black metal server maintenance workstation with the same lower-right inserted titanium root token and the same charcoal 87-key keyboard, single cable connected at the desktop right side. All geometry unchanged, only the screen glows low-intensity emerald green with a blank surface. Front three-quarter view. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 16:9 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D12 · 贺凯智能表

- 参考：无外部参考

用途／集数：E01–06；佩戴在贺凯右腕

### 可复制提示词

> One black rectangular smartwatch with a matte metal frame, black silicone strap with a single row of adjustment holes, deep black blank display, faint wear. Single object macro product photograph, empty surrounding surface. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 1:1 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D13-BACK · 裴元手机｜背面

- 参考：无外部参考

用途／集数：E03–06

使用前：附上同编号已选主卡，保持外壳、磨痕和接口。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> One dark gray unbranded smartphone approximately 15 by 7 cm, rounded metal edges, three small rear camera lenses in a vertical line at the upper left, back three-quarter view, plain back, single object. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 1:1 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-D13-FRONT · 裴元手机｜正面

- 参考：无外部参考

用途／集数：视频与毁手机动作前的屏幕底板

使用前：附上同编号已选主卡，保持外壳、磨痕和接口。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> One dark gray unbranded smartphone approximately 15 by 7 cm, rounded metal edges, single device seen from the front, blank black display, consistent edge thickness with the back-view prop. Photorealistic practical movie prop photography, soft studio lighting, seamless dark gray background, realistic material texture and subtle wear. --ar 1:1 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-S01-EMPTY-N · 总部监控大厅｜正常空景

- 参考：现有 S01-EMPTY-N，仅限梁架、灯具与地面材质

用途／集数：E01–03、06主场景

### 可复制提示词

> A corporate monitoring hall 40 meters long, 25 meters wide and 12 meters high. South ground floor view looking north. Blank 22-meter curved display on the north wall, central master console, secondary console to the west, elevator and worktable to the south, north upper gallery connected by an east staircase. Exposed dark structural beams, cool white fixtures, restrained cyan strips, matte gray flooring and glass. Photorealistic empty live-action film set, no people. --ar 16:9 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S01-R · 总部监控大厅｜崩盘红屏

- 参考：无外部参考

用途／集数：E01–05警报

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same 40 by 25 by 12 meter corporate hall, south-to-north view, 22-meter curved screen on the north wall, operator desks east and entrance west. The giant display is solid alarm crimson, blank for compositing, red reflections across the floor and metal surfaces, some cool white fill light kept on, architecture intact. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S01-G · 总部监控大厅｜恢复翠绿

- 参考：无外部参考

用途／集数：E06

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same corporate hall, south-to-north view, north-wall 22-meter curved display, central master console, western secondary console, east staircase. The curved display is bright blank emerald green, cool white working lights restored, restrained cyan edge lighting, unchanged floor reflections and architecture. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S01-CAM01 · 大厅｜踩工牌对峙底板

- 参考：按新版布局定稿的 S01-EMPTY-N

用途／集数：E01羞辱

使用前：旧图仅作材质参考，首集机位按新版布局补做。

### 可复制提示词

> Same corporate hall as S01-EMPTY-N. Keep the exposed dark beams, existing light fixtures and floor. Camera east of the north-south confrontation axis, with clear positions for the southern character on frame left and the northern character on frame right. Leave floor space for the badge and retain the southern worktable and western secondary console in their established positions. Cool white key light and cyan edge reflections. Photorealistic empty live-action film set, no people. --ar 16:9 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S01-CAM02 · 大厅｜大屏铁证底板

- 参考：无外部参考

用途／集数：E06公开铁证

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same corporate hall. Camera from the south looking north, 50mm lens, the north-wall 22-meter curved display filling the upper frame, empty lower third for later chest-up character placement. The secondary console stays west, blank low-intensity emerald screen, realistic screen reflections. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S01-CAM03 · 大厅｜北侧二层总裁看台

- 参考：按新版布局定稿的 S01-EMPTY-N

用途／集数：E01秦岚旁观

使用前：旧图仅作材质参考，首集机位按新版布局补做。

### 可复制提示词

> Same corporate hall as S01-EMPTY-N. Ground floor east-side camera angled up toward the north upper gallery, 65mm lens. Glass-and-metal railing, the same exposed structural beams, and the east staircase connecting the gallery to the ground floor. Cool white and cyan working light for shot 09. Preserve this exact geometry under red alarm light with readable face fill for shot 24. Photorealistic empty live-action film set, no people. --ar 16:9 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S02-EMPTY-N · 地下核心机房｜正常空景

- 参考：无外部参考

用途／集数：E01插镜、E02、05–06

### 可复制提示词

> An underground core server room 60 meters long, 15 meters wide and 6 meters high. Camera at the south entrance facing north, two symmetrical rows of black high-density liquid-cooled racks receding into depth. A physical control workstation centered in the aisle with its blank display facing south, recovery and wired keyboard ports on its right. Cool white inspection lights, dark gray antistatic floor tiles, a fixed storage drawer and coat hook on the west near the entrance. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S02-R · 机房｜故障空景

- 参考：无外部参考

用途／集数：E02、05

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same core server room, symmetrical black liquid-cooled racks, centered physical workstation and south entrance unchanged. Local red alarm lights, cool white overhead inspection lights still illuminate the workstation, small red rack indicators, blank dark gray screen. Intact industrial location plate, effects added separately. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S02-G · 机房｜恢复空景

- 参考：无外部参考

用途／集数：E06

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same core server room, fixed racks, central workstation, south entrance and west storage drawer unchanged. Cool white lights restored, red indicators changed to cyan green, blank emerald workstation screen, consistent cables and industrial surfaces. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S02-CAM01 · 机房｜旧键盘操作底板

- 参考：无外部参考

用途／集数：E05–06

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same core server room and central workstation. Camera southeast of the desk looking northwest, 50mm lens, medium framing with the tabletop in the lower half, empty central space for the lead operator, right-side keyboard input and recovery slot visible, space at the rear left for a keyboard handoff. Cool white overhead light mixed with red alarm reflection, racks retain their depth. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S02-CAM02 · 机房｜键盘与密钥特写底板

- 参考：无外部参考

用途／集数：E05盲敲与插密钥

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same black metal physical control workstation. Camera behind the future operator slightly to the east, 85mm close-up looking down. Tabletop fills the lower two thirds, clear space for an 87-key keyboard and two hands, fixed recovery slot on the right, empty area at the upper right for removed eyeglasses, blank black screen edge at the top. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S03-EMPTY-D · 海边防波堤｜夜钓空景

- 参考：无外部参考

用途／集数：E03

### 可复制提示词

> An old concrete breakwater in Jinhai, 100 meters long and 8 meters wide, extending north-south. Camera from the south facing north, deep navy sea and waves on the right to the east, access road on the left to the west. Damp cracked concrete, a low fishing stool and small portable folding table near the east edge, one amber camping lantern lighting the spot. Blue-black night, only the stool, table and lantern arranged at the fishing spot. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S03-W · 防波堤｜暴雨空景

- 参考：无外部参考

用途／集数：E03–04、05开头

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same north-south concrete breakwater, eastern sea on the right, western road on the left, same low stool and portable table near the east. Heavy rain, a thin layer of puddles on the ground, pronounced waves, warm amber camping lantern and cold white headlights spilling from off-camera west, blue-black sea night, an exposed outdoor set. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S03-CAM01 · 防波堤｜求救对峙底板

- 参考：无外部参考

用途／集数：E03秦岚求救

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same breakwater, camera south of the fishing spot looking north, 50mm medium framing. Clear seated-character space at screen right on the eastern sea side, clear standing-character space at screen left on the western road side, room behind for two others. Sea to rear right, warm low lantern light at the fishing spot and cold headlight backlight from the west, heavy rain. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S03-CAM02 · 防波堤｜跪递电脑底板

- 参考：无外部参考

用途／集数：E04

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same breakwater fishing spot, camera from the south looking north, 50mm slightly low framing. Clear foreground-left space for a kneeling figure holding a laptop, background-right space for a seated man, extra standing space at rear left. Small folding table nearby for signing, thin muddy water on the ground, sea at right and road at left, warm lantern versus cold rain-night backlight. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S03-CAM03 · 防波堤｜沿湾远眺大厦

- 参考：无外部参考

用途／集数：E03–04空间反差

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> A viewpoint from the end of the same concrete breakwater looking across the bay westward toward the city. 85mm distant framing, wet low concrete edge in the foreground, blue-black water and a distant skyline, one corporate tower far across the bay with faint red alarm reflections, a believable 15-kilometer distant scale. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S04-EMPTY-N · 大厦前场｜夜间空景

- 参考：无外部参考

用途／集数：E01、03、05–06

### 可复制提示词

> A modern corporate tower forecourt, glass-and-metal main entrance to the west, city road to the east, flat stone pedestrian area between, low planters to the south, vehicle entrance to the north. Camera southeast looking northwest, clear main doors, damp stone reflecting cool white entrance lights, cyan interior reflections in the glass, empty road. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S04-R · 大厦前场｜警报反射

- 参考：无外部参考

用途／集数：E01、03、05

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same tower forecourt, western entrance, eastern road, southern planters and northern vehicle access unchanged. Crimson interior alarm reflections on the glass doors and wet stone, city road visible in the background, same southeast-to-northwest camera. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S04-M · 大厦前场｜晨光尾声

- 参考：无外部参考

用途／集数：E06三倍加班费收尾

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same corporate tower entrance and pedestrian route after the rain. Early morning light from the east grazing the wet stone, the interior red alarm gone, space in the foreground for a man to walk away carrying fishing gear, quiet city waking in the background. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S04-CAM01 · 大厦前场｜离场归来

- 参考：无外部参考

用途／集数：E01、05

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same forecourt, camera on the south side facing north and slightly west, 50mm medium framing. Main glass entrance in the rear left, clear walking route through the center, road and a reserved area for vehicle lights at rear right, damp stone and realistic glass reflections. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S05-EMPTY-W · 防波堤停车带｜暴雨空景

- 参考：无外部参考

用途／集数：E03抵达、05返程

### 可复制提示词

> A parking strip on the road west of the old breakwater. Pedestrian access on the east leads onto the concrete pier, low harbor wall and road to the west. Camera southwest looking northeast, heavy rain at night, wet asphalt puddles, a distant low amber lantern toward the eastern pier, cool white road lights, a small distant glimpse of sea beyond the pier. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S05-CAM01 · 停车带｜豪车长龙底板

- 参考：无外部参考

用途／集数：E03几十辆豪车分层合成

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same harbor parking strip and eastern pedestrian entrance, camera southeast facing northwest, low 35mm framing. Clear foreground positions for two black sedans parked at angles, road receding into the background with ample space for multiple layers of headlights, eastern pedestrian entrance remains clear. Heavy rain and strong reflections on wet asphalt, empty vehicle positions. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S06-EMPTY-N · 总部会客室｜空景

- 参考：无外部参考

用途／集数：E03、06

### 可复制提示词

> A modern corporate meeting room, soundproof door on the west leading to the monitoring hall, dark glass window on the north, black wood meeting table at the center, one charcoal leather chair north of the table, two matching chairs south, fixed metal decorative lines on the east wall. Camera southwest looking northeast, warm white business lighting, faint red alarm reflections at the north window, clear tabletop. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S06-CAM01 · 会客室｜裴元视频背景

- 参考：无外部参考

用途／集数：E03视频逼宫

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same meeting room, camera south of the table looking north, 70mm chest-up composition plate with a clear central seated-character area, the same north window, east-wall metal lines and faint red reflection in the background. West door outside the left edge, warm white key light and subtle cool fill, clear tabletop. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-S06-CAM02 · 会客室｜裴元欲逃

- 参考：无外部参考

用途／集数：E06走出同一会客室

使用前：附上同一场景已选空景图，保持结构；反向机位按正文重建视角，不镜像整张图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> The same meeting room seen from the east looking west, 50mm medium framing, the west door half open in the center, a little emerald display reflection visible from the monitoring hall beyond. Clear foreground route for a man holding a phone, unchanged table, chairs and warm white room lighting. Photorealistic live-action film location, contemporary Chinese city, physically believable architecture, cinematic lighting, readable shadows, an empty set. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI people

## IMG-FX01 · 雨丝层

- 参考：无外部参考

用途／集数：E03–05

### 可复制提示词

> Cold white fine rain streaks isolated on a pure black background, falling slightly diagonally from upper left to lower right, a few thicker near-camera streaks and finer distant streaks, moderate density, only the rain layer visible. Photorealistic cinematic compositing element. --ar 9:16 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-FX02 · 车灯光晕

- 参考：无外部参考

用途／集数：E03–05

### 可复制提示词

> Two soft cold-white headlight glows isolated against pure black in the lower half of the frame, moderate separation, natural edge falloff, faint horizontal flare, only the light layer visible. Photorealistic cinematic compositing element. --ar 9:16 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-FX03 · 警报红光

- 参考：无外部参考

用途／集数：E01–05

### 可复制提示词

> Low-intensity dark crimson soft light isolated against pure black at the left and right edges, central region almost completely black, layered light falloff, only the light haze visible. Photorealistic cinematic compositing element. --ar 9:16 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-FX04 · 海边薄雾

- 参考：无外部参考

用途／集数：E03–04

### 可复制提示词

> A very thin horizontal band of cool gray sea mist isolated on pure black in the bottom third of the frame, natural fading edges, large clean black area above, only the mist visible. Photorealistic cinematic compositing element. --ar 9:16 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-FX05 · 服务器火花

- 参考：无外部参考

用途／集数：E02

### 可复制提示词

> A localized burst of orange-white electrical sparks isolated against pure black at the lower right, fine short sparks spreading outward with a trace of smoke, realistic photographic exposure, most of the frame black, only the sparks layer visible. Photorealistic cinematic compositing element. --ar 9:16 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## IMG-FX06 · 盲敲残影备选素材

- 参考：无外部参考

用途／集数：E05–06

使用前：附P01挽袖手腕图与D02键盘图。 当前尚无已生成参考图；此行是生成顺序说明。

### 可复制提示词

> One pair of adult male hands above one charcoal 87-key mechanical keyboard with gray-white blank keycaps, charcoal hoodie sleeves pushed to mid-forearm, dark mechanical watch on the left wrist, subtle sideways photographic motion trails around the moving fingers, two clearly readable physical hands, the keyboard outline stable, center spacebar worn patch visible. Isolated against pure black, close-up practical effect photography. Photorealistic cinematic compositing element. --ar 9:16 --raw --s 25 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

## 后期与连续性固定表（不复制进Midjourney）

| 内容 | 固定口径 |
|---|---|
| 正片画幅 | 9:16；三视图和宽道具横图仅作参考素材 |
| 时钟 | 1800秒→600秒→海边180秒→“线程挂起”→机房最后10秒→01秒全绿；返程保持挂起 |
| 合同 | 15%集团无偿干股、技术一票否决权；原台词“先签期权转让书”不改 |
| 证据 | 五千万美金交易、前两集贺凯看表时间与交易时间并列；公开铁证与警方带走沿企划 |
| 工牌与密钥 | 原工牌裂壳、周衍捡走钛合金内芯、E05插主柜；金质新工牌是另一件物品 |
| 旧键盘 | E01交唐小川并装入背包；后续须交代转存固定抽屉；E05取出，接同一根线；空格磨痕、右上划痕不换位 |
| 身份与强弱 | 三层身份、十六进制热补丁、踢膝跪递电脑、魏哲跪拜、火花、盲敲残影均沿原企划 |
| 文字政策 | 编号0001、盘古AI、报错、倒计时、合同、签名、转账和股价暴跌40%均后期制作 |
| 后期图层 | FX为纯黑底素材，黑底不等于透明底；雨、灯与火花按遮挡合成。FX06优先用已生成盲敲镜头的延迟帧叠加，本提示词只作备选。 |

场景正反打仍使用世界方位。S03朝北海在画右，朝南海在画左；人物的右眉、左眼下痣、左右手表和键盘出线不能随镜头镜像。MJ可能漏画或移动细节，选图时逐项检查；仅凭相同英文描述不代表身份已锁定。

需要单独修正侧面时，在V8.2附上选定人物图后可另用：

> Show the same person in a left-side profile, preserving facial identity, age, hairstyle, glasses and the original outfit. Full body, head and shoes visible, relaxed standing pose, seamless light gray studio background, soft even photographic lighting. --ar 9:16 --raw --s 50 --v 8.2 --no text logos watermarks anime cartoon illustration CGI

此行是修正操作示例，不是新增人物卡。脸、服装、空间与道具均需通过实际生成确认；本文件未宣称Midjourney可精确复刻每个细节。

## 官方用法来源

查询日期：2026-11-04。项目提示词为依据资产库编写的原创内容；以下仅用于核对参数和参考图操作。

- [Parameter List](https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List)
- [Raw](https://docs.midjourney.com/hc/en-us/articles/32634113811853-Raw)
- [Stylize](https://docs.midjourney.com/hc/en-us/articles/32196176868109-Stylize)
- [Version](https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version)
- [Edit Model](https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model)

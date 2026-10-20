# 台词与旁白 JSON

用于配音清单和程序导入。它把当前文本按说话人、声音类型和情绪切分，不承担故事改写。先确定输入是原著，还是当前版本 `剧本.md`；结果只与这一份来源核对。

## 可复制提示词

````text
请把下面的来源文本转换为JSON数组，用于台词/旁白整理，只做结构化，不润色、不新增或调换来源文字。

输入：
来源文本：【粘贴文本或填写文件路径与范围】
角色表：【CHAR-001=林岚；CHAR-002=周叔；按实际替换】
文稿类型：【连续叙事正文 / 含镜号和舞台说明的剧本】
输出范围：【全文声音与叙事文本 / 仅剧本中显式标出的对白、旁白、内心独白】
长度上限：【默认50个Unicode字符，含标点；短句不补字、不强行凑35字】

规则：
1. 先识别来源中明确的说话人与引语边界。双引号、冒号、破折号只是线索，不能单靠标点判断；环境、动作、心理叙述不能误标为别人的对白。
2. 文稿类型为连续叙事正文且范围为全文时，所有原文字符都必须进入text_content，连换行和引号也保留。记录按原顺序拼接后必须与输入原文逐字符一致。
3. 若输入为带镜号和舞台说明的剧本，只把所选声音范围导出，镜号、字段标签和动作栏不读入配音；在source_ref注明来源位置，不声称JSON覆盖了整个剧本全文。
4. 不修改中英文引号、全半角、空白或标点。JSON语法需要的转义由序列化处理，解析后的text_content仍应是原字符。
5. 同一条记录仅有一个说话人和一种声音类型。按句义切分长文本；同一句超过上限时优先在标点或从句处分开，必要时在字符边界切开并标记延续，不丢任何字符。
6. 字符位置start/end使用从0开始的Unicode码点索引，左闭右开；范围对应完整来源文本，包括未导出的舞台说明。起止位置能定位原文，不用UTF-8字节数或UTF-16代码单元数。
7. 角色未知时role_id=null、role_name="待确认"，issue写明需确认的线索。旁白用role_id=null、role_name="旁白"。不要为了填表捏造角色。
8. emotion_name从[高兴,生气,伤心,害怕,厌恶,低落,惊喜,平静]选择；strength_name从[微弱,稍弱,中等,较强,强烈]选择。未明确时旁白可用平静/中等，人物按上下文判断，判断不改变原文。
9. speech_type仅用dialogue、narration、inner_voice。内心独白与旁白均不要求画面角色做口型。
10. 输出合法JSON数组，不加Markdown围栏或解释。输入不足以处理时先说明缺项，不输出伪造结果。

每条记录字段：
{
  "segment_id": "TXT-001",
  "role_id": "CHAR-001或null",
  "role_name": "角色名/旁白/待确认",
  "speech_type": "dialogue/narration/inner_voice",
  "text_content": "来源原字符",
  "emotion_name": "平静",
  "strength_name": "中等",
  "continues_previous": false,
  "source_ref": {"start": 0, "end": 0},
  "issue": null
}

segment_id中的TXT编号只用于导出文本记录，不代替视频SEG编号。continues_previous只在同一原句被长度上限拆开时设true，不把相邻的不同句子一概视为延续。
````

## 正确示例

来源正文（单行，无末尾换行）：

```text
林岚停在门前。“钥匙呢？”她问。周叔把钥匙递给她。
```

角色表：`CHAR-001=林岚`，`CHAR-002=周叔`。输出范围选全文。引号保留在对白里，“她问。”属于叙述。

```json
[
  {
    "segment_id": "TXT-001",
    "role_id": null,
    "role_name": "旁白",
    "speech_type": "narration",
    "text_content": "林岚停在门前。",
    "emotion_name": "平静",
    "strength_name": "中等",
    "continues_previous": false,
    "source_ref": {"start": 0, "end": 7},
    "issue": null
  },
  {
    "segment_id": "TXT-002",
    "role_id": "CHAR-001",
    "role_name": "林岚",
    "speech_type": "dialogue",
    "text_content": "“钥匙呢？”",
    "emotion_name": "平静",
    "strength_name": "中等",
    "continues_previous": false,
    "source_ref": {"start": 7, "end": 13},
    "issue": null
  },
  {
    "segment_id": "TXT-003",
    "role_id": null,
    "role_name": "旁白",
    "speech_type": "narration",
    "text_content": "她问。周叔把钥匙递给她。",
    "emotion_name": "平静",
    "strength_name": "中等",
    "continues_previous": false,
    "source_ref": {"start": 13, "end": 25},
    "issue": null
  }
]
```

仅在下游明确要求其他字段名时做一次格式转换，不修改这份导出中的角色归属或文本。配音时是否读出书名号、引号等符号，由配音工具处理，不通过改写原文隐式解决。

## 使用前核对

- JSON能解析；字段类型正确；`null`不是字符串。
- 来源片段和起止索引逐条一致，角色与声音类型吻合。
- 全文模式下，索引连续且覆盖完整来源，`text_content`拼接等于原文。
- 仅声音模式下，只核对选中的声音范围，动作和标签不混入配音。
- 所有记录不超长度上限，短句不被补长，没有无来源的新台词。

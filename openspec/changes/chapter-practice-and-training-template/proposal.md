## Why

当前仓库已形成 day 学习总结流程，但“强化训练”仍主要散落在 day 文档中，缺少按章节沉淀的题库与答案结构，导致复用、检索和持续进阶效率不稳定。现在需要把训练内容从“临时记录”升级为“可持续训练资产”。

## What Changes

- 新增按章节与难度组织的训练目录规范：`practice/<章节>/{foundation,advanced,transfer}`。
- 新增与训练目录镜像的答案目录规范：`answers/<章节>/{foundation,advanced,transfer}`。
- 新增统一题号与文件命名规则：`p-xxx-topic.md` 与 `p-xxx-topic.answer.md`。
- 修改 day 模板要求：强化训练必须包含题目、验收标准、答案回链路径。
- 新增 day 与训练题目的回链规则，确保每天学习内容可定位到对应训练与答案。

## Capabilities

### New Capabilities
- `chapter-practice-structure`: 定义并约束按章节+难度分层的训练与答案目录结构及命名规则。

### Modified Capabilities
- `daily-timeline-backfill`: 扩展 day 输出要求，新增“强化训练回链字段”与答案路径引用约束。

## Impact

- 影响目录：仓库根目录新增 `practice/` 与 `answers/` 结构（按章节与难度分层）。
- 影响文档：`daily/templates/day-template.md` 与现有 day 文档回链字段。
- 影响流程：day 产出从“只总结”升级为“总结+训练+答案回链”。

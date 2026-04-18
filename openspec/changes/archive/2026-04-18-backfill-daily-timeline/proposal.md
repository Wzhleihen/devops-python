## Why

仓库已完成目录归档与 daily 入口建立，但历史学习内容尚未沉淀为连续 `dayxx.md` 时间线，导致“按天复盘”和“按章节回链”仍依赖手工检索。现在补全全历史 daily 时间线，可以把 GitHub 历史与章节学习内容连接起来，提升学习效率与可追溯性。

## What Changes

- 基于 GitHub 全历史提交记录提取日期时间线，并与当前仓库目录状态做对齐。
- 建立 `day01..dayNN` 的连续编号映射规则（从最早历史日期递增）。
- 在 `daily/` 下批量生成历史 day 文档初稿，使用统一模板并保留章节回链字段。
- 对“低信息量日期”定义合并或占位策略，避免生成空洞日记。
- 生成补全过程的校验机制（编号连续、路径有效、模板字段完整）。

## Capabilities

### New Capabilities
- `daily-timeline-backfill`: 从 GitHub 历史自动补全 daily 时间线并生成规范化 day 文档初稿。

### Modified Capabilities
- None.

## Impact

- 影响范围：`daily/` 目录内容、模板应用流程、学习时间线索引。
- 不影响范围：章节目录内代码与 notebook 内容、归档目录原始文件结构。
- 依赖：本地 `gh` 可用并具备读取仓库历史权限。

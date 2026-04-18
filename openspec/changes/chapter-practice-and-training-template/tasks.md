## 1. 目录与命名规范落地

- [x] 1.1 创建 `practice/<章节>/{foundation,advanced,transfer}` 目录骨架
- [x] 1.2 创建 `answers/<章节>/{foundation,advanced,transfer}` 目录骨架
- [x] 1.3 定义并固化题号命名规则（`p-xxx-topic` 与 `.answer.md` 对应）

## 2. Day 模板强化训练联动

- [x] 2.1 更新 `daily/templates/day-template.md`，将训练题目与答案路径设为必填
- [x] 2.2 增加 day 文档中的训练回链格式约束（practice/answers 对应）
- [x] 2.3 提供一组标准训练区块示例（基础/进阶/迁移）

## 3. 校验机制

- [x] 3.1 实现题目-答案配对校验（同题号同 topic）
- [x] 3.2 实现训练路径有效性校验（practice 与 answers 路径存在）
- [x] 3.3 实现章节内题号唯一性校验

## 4. 首批内容与迁移策略

- [x] 4.1 为至少 2 个章节各生成 3 题（foundation/advanced/transfer）样例
- [x] 4.2 为样例题补全对应答案文件
- [x] 4.3 在 day 文档中增加样例题回链并验证可定位

## 5. 集成与验收

- [x] 5.1 提供一键检查入口并输出结构化报告
- [x] 5.2 验证“归档先不用写”约束未被破坏
- [x] 5.3 输出最终验收清单（目录完整、命名合规、回链有效）

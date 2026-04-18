---
template: day-log
version: v2
required:
  - DAY
  - DATE
  - GAP
  - TOPIC
  - CHAPTER_CN
  - SECTION
  - LESSON_INDEX
  - CODE_PATHS
  - PRACTICE_FILES
  - ANSWER_FILES
  - ONE_ERROR
  - NEXT_STEP
  - TRAINING_GOAL
  - TRAINING_TASKS
  - TRAINING_ACCEPTANCE
  - TRAINING_ANSWER_LINKS
  - TRAINING_REVIEW_RULES
---

# Day {{DAY}} - {{TOPIC}}

📅 日期：{{DATE}}  
⏱ 距离上次学习：{{GAP}} 天

---

## ✅ 今日目标

- [ ] 目标1：{{GOAL_1}}
- [ ] 目标2：{{GOAL_2}}
- [ ] 目标3（可选）：{{GOAL_3}}

## 📚 章节内容

- 章节：{{CHAPTER_CN}}
- 小节：{{SECTION}}
- 学习位置：{{LESSON_INDEX}}
- 对应练习：{{PRACTICE_FILES}}
- 对应答案：{{ANSWER_FILES}}
- 章节总结（3行内）：
  1. {{CHAPTER_SUMMARY_1}}
  2. {{CHAPTER_SUMMARY_2}}
  3. {{CHAPTER_SUMMARY_3}}

## 📌 今日内容

- {{TODAY_WORK_1}}
- {{TODAY_WORK_2}}
- {{TODAY_WORK_3}}

## 🧠 核心知识

- 概念：{{CONCEPT}}
- 机制：{{MECHANISM}}
- 场景：{{SCENARIO}}

## 💻 关键代码（最小可运行）

```python
{{KEY_CODE_SNIPPET}}
```

- 代码行为解释：
  - 输入：{{INPUT_DESC}}
  - 输出：{{OUTPUT_DESC}}
  - 关键点：{{KEY_POINT_DESC}}

## ⚠️ 问题 / 坑（至少1个）

- 错误现象：{{ERROR_SYMPTOM}}
- 根因分析：{{ROOT_CAUSE}}
- 修正方式：{{FIX}}
- 防再犯规则：{{PREVENTION_RULE}}

## 🧩 我的理解（第一人称）

- 我现在能清楚解释：{{I_CAN_EXPLAIN}}
- 我还模糊的点：{{I_STILL_CONFUSED}}
- 我准备怎么补：{{HOW_TO_IMPROVE}}

## 🚀 延伸

- 下一步学习：{{NEXT_STEP}}
- 预计投入：{{NEXT_DURATION}}
- 预期产出：{{NEXT_OUTPUT}}

## 🏋️ 强化训练（练习 / 答案 / 要求）

- 训练目标：{{TRAINING_GOAL}}
- 训练任务：
  1. {{TRAINING_TASK_1}}
  2. {{TRAINING_TASK_2}}
  3. {{TRAINING_TASK_3}}
- 难度分层：{{TRAINING_LEVELS}} （示例：基础 / 进阶 / 迁移）
- 验收要求：
  - {{TRAINING_ACCEPT_1}}
  - {{TRAINING_ACCEPT_2}}
  - {{TRAINING_ACCEPT_3}}
- 提交规范：{{TRAINING_SUBMIT_RULE}}
- 参考答案路径：{{TRAINING_ANSWER_LINKS}}
- 训练回链规范：每个训练任务至少包含 1 条 `practice/<章节>/<level>/p-xxx-topic.md` 与对应 `answers/<章节>/<level>/p-xxx-topic.answer.md`
- 复盘规则：{{TRAINING_REVIEW_RULES}}

## 📎 回链索引

- 章节目录：{{CHAPTER_PATH}}
- 关键代码：{{CODE_PATHS}}
- 练习路径：{{PRACTICE_FILES}}
- 答案路径：{{ANSWER_FILES}}
- 相关归档（可选）：{{ARCHIVE_LINKS}}

## ✅ 完成度自检（打勾）

- [ ] 本文已包含章节名与小节名
- [ ] 本文已包含至少1段关键代码
- [ ] 本文已包含至少1个错误案例（现象+根因+修正）
- [ ] 本文已写明下一步且可执行
- [ ] 已包含强化训练（目标/任务/验收/答案/复盘）
- [ ] 所有路径可点击或可定位

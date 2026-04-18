# Day 12 - `Path.parents`、`joinpath` 与目录创建（归档优先时间线版）

日期：2025-12-15  
距离上次学习：1 天

---

## 今日目标
- [x] 掌握 `Path.parent`、`Path.parents`、`parts` 的层级语义。
- [x] 区分 `joinpath()` 与 `/` 拼接在可读性上的使用场景。
- [x] 能正确使用 `mkdir(parents=True, exist_ok=True)` 处理多级目录。

## 章节内容
- 章节：文件IO（`pathlib` 进阶）
- 小节：
  1) 路径层级访问：`parent` / `parents`  
  2) `joinpath` 与 `/` 的工程写法  
  3) 目录创建与存在性判断
- 学习位置：`文件IO/文件IO.ipynb`
- 对应练习：`文件IO/文件IO.ipynb`
- 章节总结（3行内）：
  1. 重点从“会拼接路径”升级到“会分析路径结构”。
  2. 增加了目录创建、遍历、通配查找等实操。
  3. 这一天是连接路径知识与文件系统操作的关键过渡。

## 证据来源（归档优先）
- 归档检查：未发现 `归档/2025/2025-12-15`（归档缺失）。
- 补证来源：
  - `文件IO/文件IO.ipynb`
  - 提交证据：
    - `e4f0539d7c947120db859bc2a5cd9947cd5b289a`（update parents and path joining examples）
    - `6192f8fedabbdcd4899243114968b3fb56cc4107`（update pathlib examples one end）
    - `32efce41a6234a2f02c788ccf5055bea2ffbb526`（update pathlib usage examples）

## 今日内容（代码在做什么）
1. 读取 `p.parent` 与遍历 `p.parents`，观察路径逐级回溯结果。  
2. 练习 `parts` 拆分、`joinpath()` 合并、`glob/rglob` 查找。  
3. 通过 `p3.mkdir(parents=True, exist_ok=True)` 创建多级目录并避免重复创建报错。  
4. 用 `iterdir()` 判断目录是否为空，实现目录状态检查。

## 核心知识（底层原理）
- `parent` 是单级回溯，`parents` 是可迭代的祖先链。
- `joinpath()` 在多参数拼接时语义更直观，`/` 更适合短链表达。
- `mkdir(parents=True)` 负责递归创建父目录，`exist_ok=True` 负责“已存在时不报错”。
- 路径 API 与文件系统 API 结合时，要先做存在性与类型判断（`exists/is_dir/is_file`）。

## 问题 / 坑（真实错误案例）
### 案例：已存在目录重复创建的报错风险
- 错误现象：当目录已存在且使用 `mkdir(parents=True)`（未加 `exist_ok=True`）时，会触发目录已存在错误。  
- 根因：目录创建 API 默认要求目标不存在。  
- 修正方式：
  ```python
  p3.mkdir(parents=True, exist_ok=True)
  ```
- 防再犯规则：批量/重复执行场景默认加 `exist_ok=True`，并配合 `exists()` 做幂等检查。

## 强化训练（练习 / 答案 / 要求）
- 训练目标：形成可复用的路径结构分析与目录操作模板。
- 训练任务：
  1. 基础：给定任意路径，输出 `name/stem/suffix/parent/parents`；  
  2. 进阶：实现 `ensure_dir(path)`，满足幂等创建；  
  3. 迁移：实现 `scan_py_files(root)`，返回 `rglob('*.py')` 结果及文件大小。
- 验收要求：
  - 至少覆盖“目录已存在”和“目录不存在”两种分支；
  - 结果输出包含路径对象和字符串表示两种格式；
  - 提交时附一条异常分支处理说明。
- 参考路径：`文件IO/文件IO.ipynb`
- 训练回链：`practice/文件IO/advanced/p-002-copytree-filter.md`
- 答案回链：`answers/文件IO/advanced/p-002-copytree-filter.answer.md`

## 我的理解（第一人称）
- 我现在能清楚解释：`parent`、`parents`、`joinpath`、`mkdir` 在一条工作流里的配合关系。  
- 我还模糊的点：跨系统（Windows/Linux）路径差异在复杂脚本中的最佳抽象层。  
- 我准备怎么补：把路径处理统一沉淀为工具函数，减少散落写法。

## 回链索引
- 关键文件：`文件IO/文件IO.ipynb`
- 关键提交：
  - `e4f0539d7c947120db859bc2a5cd9947cd5b289a`
  - `6192f8fedabbdcd4899243114968b3fb56cc4107`
  - `32efce41a6234a2f02c788ccf5055bea2ffbb526`
- 证据说明：本日无对应归档目录，已按规则使用补证来源。

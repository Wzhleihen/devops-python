# P-010 OOP 综合迁移训练（Temperature + Shape + Mixin + argparse）

📎 回链：`daily/day24.md`  
🎯 层级：transfer  
📅 日期：2026-04-28

---

## 题目

### 第一题：Temperature 增强

在已有 Temperature 类基础上，增加以下功能：
1. 实现 `__repr__`，输出格式：`Temperature(20.0°C / 68.0°F / 293.15K)`
2. 实现 `__eq__`，两个 Temperature 对象在摄氏温度相等时视为相等
3. 实现 `__add__`，支持两个 Temperature 相加（以摄氏度为基准）

**验收标准**：
- [ ] `repr(Temperature(100))` 输出包含三种温度
- [ ] `Temperature(0) == Temperature(32, 'f')` 为 True
- [ ] `Temperature(20) + Temperature(30)` 结果的 `.c` 为 50

### 第二题：Shape + PerimeterMixin

扩展 Shape 体系：
1. 创建 `PerimeterMixin`，提供 `perimeter` 属性（周长），使用 `_perimeter` 缓存
2. 创建 `FullTriangle(PerimeterMixin, Triangle)`，同时具备面积和周长
3. 创建 `FullCircle(PerimeterMixin, Circle)`，同时具备面积和周长

**验收标准**：
- [ ] `FullTriangle(3,4,5).perimeter` 返回 12
- [ ] `FullCircle(5).perimeter` 返回 `2 * pi * 5`
- [ ] 打印 `FullTriangle.mro()` 并解释每一层的职责

### 第三题：argparse + pathlib 实现简化 find

用 argparse 实现简化版 `find` 命令：
- 位置参数：搜索路径（默认 `.`）
- `-name PATTERN`：按文件名模式过滤（支持 `*` 通配符）
- `-type f|d`：过滤文件类型（f=文件，d=目录）
- 输出：每行一个匹配路径

**验收标准**：
- [ ] `find . -name "*.py" -type f` 能列出当前目录下所有 .py 文件
- [ ] 使用 `pathlib.Path.rglob()` 实现递归搜索
- [ ] 不使用 `os.walk`，全程 pathlib

# p-008-init-override-mixin-mro

## 训练目标
围绕“继承初始化 + 方法重写 + Mixin 组合”建立可调试的机制理解，能用输出验证调用顺序。

## 题目要求
1. 定义 `A` 与 `B(A)`：在 `B.__init__` 中先故意不写 `super()`，复现父类属性缺失报错；再给出修复版本。  
2. 定义 `Animal` 与 `Dog(Animal)`：`Dog.shout` 必须先调用父类逻辑，再打印子类扩展输出。  
3. 定义 `Document`、`PrintableMixin`、`PrintableWord(PrintableMixin, Document)`，输出 `PrintableWord.__mro__` 并解释 `print` 方法命中路径。  
4. 在一个脚本里串联以上三部分，保证可直接运行。

## 验收标准
- 必须包含“错误复现 + 修复后”两段输出；
- 必须至少 2 次使用 `super()`（一次在 `__init__`，一次在普通方法）；
- 必须输出并解释一次 MRO；
- 代码可运行，无语法错误。

## 提交产物
- 脚本文件（建议：`init_override_mixin_demo.py`）
- 运行输出（终端文本或截图）

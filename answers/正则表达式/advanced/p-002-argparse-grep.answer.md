# 答案：p-002-argparse-grep

## 参考实现思路
1. `argparse` 定义参数：`pattern`、`file`、`-i`。
2. 编译正则：`re.compile(pattern, re.I if args.i else 0)`。
3. 遍历文件逐行匹配并打印 `line_no: content`。

## 验收提示
- 空文件与无匹配场景也应输出明确结果（如 count=0）。

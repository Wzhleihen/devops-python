# 答案：p-003-log-analyzer

## 参考实现思路
1. 用正则分别匹配 `ERROR|WARN|INFO` 并计数。
2. 用命名分组提取 ERROR 的 `timestamp` 与 `module`。
3. 使用 `json.dumps(..., ensure_ascii=False, indent=2)` 输出摘要。

## 验收提示
- 输出 JSON 需含 `counts` 与 `errors` 两个顶级字段。

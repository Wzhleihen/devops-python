# P-009 logging 三层体系基础训练

📎 回链：`daily/day24.md`  
🎯 层级：foundation  
📅 日期：2026-04-28

---

## 题目

### 第一题：Logger + Handler + Formatter 基础配置

编写一个脚本，要求：
1. 创建一个名为 `"myapp"` 的 logger
2. 给它挂载两个 handler：
   - `StreamHandler`：输出到控制台，格式为 `[时间] [级别] 消息`
   - `FileHandler`：输出到 `app.log` 文件，格式为 `时间 | 名称 | 级别 | 消息`
3. 设置 logger 级别为 `DEBUG`
4. 分别发送 `debug/info/warning/error` 四条消息

**验收标准**：
- [ ] 控制台和文件各输出 4 条日志
- [ ] 两个 handler 的格式不同
- [ ] `app.log` 文件内容可读

### 第二题：EffectiveLevel 验证

编写代码验证 EffectiveLevel 的向上查找机制：
1. 获取 root logger，设置级别为 `WARNING`
2. 创建子 logger `"myapp"`，**不设置**级别
3. 创建孙 logger `"myapp.db"`，**不设置**级别
4. 打印三者的 `level` 和 `getEffectiveLevel()` 并解释差异

**验收标准**：
- [ ] `myapp` 和 `myapp.db` 的 `level` 为 0（NOTSET）
- [ ] `myapp` 和 `myapp.db` 的 `getEffectiveLevel()` 为 30（WARNING）
- [ ] 能用文字说明 EffectiveLevel 的查找路径

### 第三题：避免 Handler 重复挂载

写一个函数 `setup_logger(name)`，要求：
- 多次调用时不会重复添加 handler
- 提示：利用 `logger.handlers` 检查

**验收标准**：
- [ ] 调用 3 次 `setup_logger("test")` 后，`logger.handlers` 长度仍为预期值

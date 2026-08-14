# 实验状态与证据

状态含义：

- `DESIGNED`：步骤和验收已定义；
- `CODE_READY`：代码已完成静态检查，尚未在锁定DSH组合中验证；
- `VERIFIED`：已按记录环境执行且证据通过；
- `BLOCKED`：外部依赖或已知问题阻止执行。

| 实验 | 状态 | 当前证据 | 下一门禁 |
|---|---|---|---|
| Lab 01 源码地图 | DESIGNED | 三阶段实验、反事实验证、证据模板与12分量表 | 保存真实`dump-config`、能力关系图和反事实运行证据 |
| Lab 02 问候工具 | CODE_READY | 示例基于官方`defineTool`教程接口 | 在`0.1.0-rc.5` Web Profile调用并保存事件 |
| Lab 03 事件观察器 | CODE_READY | 使用官方`session/event`监听形式 | 运行一次工具turn并验证事件配对 |
| Lab 04 受控Data Agent | CODE_READY | 无依赖单元测试随仓库提供 | CI运行并保存通过记录 |
| Lab 05 插件审查 | DESIGNED | 十项审查模板 | 完成首个真实社区插件报告 |

> 首个版本不虚构外部运行结果。后续每次把状态升级为`VERIFIED`，必须在PR中附带日志或机器可读报告。

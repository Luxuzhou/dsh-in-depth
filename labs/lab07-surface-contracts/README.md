# Lab 07：三种 Surface 的契约对照

## 问题

使用 Web、Headless 和 Python SDK 对同一个只读仓库执行“定位失败测试并给出原因”，验证 Surface 变化是否改变核心 Agent 契约。

## 固定条件

固定 DSH、模型、Prompt、Workspace 快照、Agent 配置和工具集合；分别保存三个 Profile 的 `--dump-config` 和工具 Schema。若某 Surface 不支持交互式审批或澄清，预先定义 fail-closed 行为。

## 对照项

- 请求身份怎样映射到 Agent/Session；
- 流式事件、工具 call/result 和结束原因；
- 审批、澄清与取消如何表达；
- Artifact/Workspace 的真实所有者；
- 恢复同一 Session 时模型可见历史；
- 最终证据是否指向同一失败测试；
- 延迟、Token、工具次数和错误。

## 故障注入与验收

中断客户端连接、取消长工具、重启 Runtime、提交重复请求、尝试用另一个身份恢复 Session。核心结论应语义一致；差异必须能由 Profile、Surface 能力或身份策略解释。报告给出企业网关、外置状态与多租户隔离还需补哪些组件。

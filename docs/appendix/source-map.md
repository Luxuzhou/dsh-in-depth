# 源码阅读地图

不要从仓库第一行顺序读到最后一行。按照问题选择入口，再沿配置、服务、事件和消费者追踪。

| 想回答的问题 | 先读文档 | 再看源码 |
|---|---|---|
| 整体如何组合 | `docs/architecture.md` | `packages/bundle`、`apps/cli` |
| 插件如何运行 | `docs/cordis-primer.md` | `vendor/cordis` |
| 一轮任务如何推进 | `docs/agent-lifecycle.md` | `packages/core/agent-loop` |
| 会话如何回放 | `docs/subsystems/session.md` | `packages/core/session`、`packages/session` |
| 工具如何执行 | `docs/tool-execution-pipeline.md` | `packages/core/tools` |
| Skill如何发现 | `docs/subsystems/skills.md` | `packages/skill` |
| Web如何访问后端 | `docs/api-gateway.md` | `packages/api`、`packages/client`、`apps/web` |
| 如何打包插件 | `docs/user/develop/basic/publish.md` | `packages/bundle`、Profile管理代码 |

## 阅读记录模板

```markdown
- 问题：
- 上游提交：
- 配置入口：
- 服务键：
- 事件：
- Provider：
- Consumer：
- 持久状态：
- 失败方式：
- 测试证据：
- 尚未确认：
```

把“尚未确认”单列，可以防止源码猜测逐渐被写成事实。

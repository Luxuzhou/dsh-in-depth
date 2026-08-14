# 深入理解 DeepSeek Harness

> 从代码框架、插件生态到生产实践的开源项目书籍

本书面向第一次接触 Agent Harness 的开发者、希望构建插件的工程师，以及准备 AI Agent、平台工程和应用架构岗位的求职者。它不把 DSH 当作一个黑盒工具，而是沿着“概念 → 源码 → 实验 → 生产判断”的路径解释：一个模型如何通过上下文、工具、会话和插件成为可运行的 Agent 系统。

当前版本基于 DeepSeek Harness `0.1.0-rc.5`、提交 [`47f9438`](https://github.com/deepseek-ai/deepseek-harness/tree/47f943859bef60e4160492346772ded9b24f765a)。官方仍将 DSH 标记为 Developer Preview，因此本书固定源码基线，并将变化显式记录到[兼容性矩阵](docs/appendix/compatibility.md)，不把易变 API 写成永久事实。

## 核心公式

```text
DSH 应用 = 插件树 + Agent Loop + 会话事件 + 能力接缝 + 产品界面
```

## 全书结构

| 章 | 主题 | 完成后能够 |
|---|---|---|
| 1 | 从模型到 Harness | 建立 DSH 的整体心智模型 |
| 2 | Cordis 微内核 | 读懂插件、Context、Service、Effect |
| 3 | Agent 生命周期 | 沿源码追踪一轮任务如何运行 |
| 4 | 会话与上下文 | 区分持久事实、实时控制和模型历史 |
| 5 | 工具与安全策略 | 编写工具并理解审批、取消与展示 |
| 6 | 插件、Bundle 与 Profile | 打包、安装和组合一个插件 |
| 7 | Skills、MCP 与工作流 | 选择扩展机制，避免能力重复建设 |
| 8 | Web、SDK 与部署 | 从本地 Web 走向可集成服务 |
| 9 | 生态与生产化 | 审查社区插件并建立生产门禁 |
| 10 | Data Agent 案例 | 设计可靠的企业智能问数系统 |

每章均按“问题—机制—源码证据—失败模式—实验—生产边界”展开，并包含源码路标、思考题和求职面试题。七个配套实验位于 [`labs/`](labs/)，实验是否真正执行、需要什么环境以及证据位置记录在 [`docs/LAB_STATUS.md`](docs/LAB_STATUS.md)。内容门禁会阻止章节退化为短提纲，但不能替代技术审校和真实实验。

## 阅读路线

- 初学者：引言 → 第 1、2、3、5、6 章 → Lab 01、02。
- 插件作者：第 2、5、6、7、9 章 → Lab 02、03、05、06。
- 企业架构师：第 3、4、5、8、9、10 章 → Lab 04、07。
- 求职准备：完成一条上述路线，再阅读[岗位能力地图](docs/career/roadmap.md)并提交一个可演示项目。

## 本地阅读

```bash
uv sync --extra docs
uv run mkdocs serve
```

打开 `http://127.0.0.1:8000`。不安装依赖也可以直接在 GitHub 阅读 Markdown。

生成单卷Markdown书稿：

```bash
python scripts/export_book.py
```

推送`v*`标签后，Release工作流使用同一正文生成Markdown、EPUB和PDF。Windows环境在Actions不可用时可运行`scripts/publish_pages.ps1`手动更新在线站点。

## 项目原则

1. 以官方源码和官方文档为第一手依据。
2. 固定上游提交；更新基线必须同时更新兼容性说明和实验状态。
3. 区分“官方保证”“源码观察”“社区实践”“作者建议”。
4. 克隆成功不等于实验完成，只有保存验收证据才标记为通过。
5. 教学示例追求最小可解释，生产章节明确补充权限、审计和故障边界。

## 参与贡献

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。书籍写作范式受到《[深入理解 AI Agent](https://github.com/bojieli/ai-agent-book)》启发；正文和代码均为本项目重新组织、独立撰写。

## 许可

MIT License。引用第三方项目时，其代码和文档仍遵循原项目许可。

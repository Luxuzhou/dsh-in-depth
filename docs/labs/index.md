# 配套实验

实验用于验证正文中的行为，不以“代码文件存在”代替真实运行证据。每个实验包含目标、前置条件、步骤、验收和延伸任务。

## Lab 01：源码地图与运行配置 {#lab-01}

**难度：★★　状态：深度实验设计完成，待跨平台执行**

1. 固定环境与上游提交，运行`dsh --profile web --dump-config`保存有效插件树。
2. 任选文件、Shell或Session能力，找到Definition、Provider、Consumer、Policy和Environment。
3. 追踪一次turn/step轨迹，区分持久事实与实时控制事件。
4. 通过移除或替换一项配置做反事实实验，比较预测与真实结果。
5. 重复装载/卸载，检查工具、监听器和外部资源是否正确清理。

验收产物：环境记录、`config-tree.txt`、带固定源码证据的Mermaid图、反事实报告和生产边界结论。实验按12分量表验收，10分视为完成；禁止只提交目录截图。

详见 [`labs/lab01-source-map/README.md`](https://github.com/luxuzhou/dsh-in-depth/tree/main/labs/lab01-source-map)。

## Lab 02：可配置问候工具 {#lab-02}

**难度：★★　状态：代码完成，待在锁定DSH基线上实跑**

实现一个`greet`工具，验证参数Schema、配置默认值、工具调用、模型可见结果和插件热替换；再从 overlay 推进到 Bundle/Profile，检查制品、有效配置和卸载。

验收：有效调用返回配置化问候；缺少`name`被Schema拒绝；非法配置不替换最后一个可用实例；三次重载后工具没有重复注册；卸载后工具与配置行消失。

详见 [`labs/lab02-greet-tool/README.md`](https://github.com/luxuzhou/dsh-in-depth/tree/main/labs/lab02-greet-tool)。

## Lab 03：会话事件观察器 {#lab-03}

**难度：★★　状态：代码完成，待组合测试**

监听`session/event`，只输出结构化标识和类型，不记录用户正文和工具敏感结果。执行自然完成、工具 continuation、pre-step 拒绝和主动取消四条轨迹，再构造重复/截断事件验证投影。

验收：每个打开的turn和step都有对应结束事件；工具call/result能够配对；取消真正收敛；投影可幂等重建；观察器卸载后停止输出。

详见 [`labs/lab03-session-observer/README.md`](https://github.com/luxuzhou/dsh-in-depth/tree/main/labs/lab03-session-observer)。

## Lab 04：受控 Data Agent {#lab-04}

**难度：★★★　状态：本地无依赖测试可运行**

用内存目录模拟“检验量”存在多种业务口径。系统必须先生成结构化状态和QueryPlan；存在歧义时拒绝执行；确认口径后签发绑定计划哈希的一次性审批；计划变化后旧审批失效。

运行：

```bash
python labs/lab04-governed-data-agent/test_mock_data_agent.py
```

深度扩展加入租户/会话/状态版本/有效期绑定、并发消费、语义与权限版本失效、结构化失败和HTTP语义服务故障注入。

## Lab 05：插件审查报告 {#lab-05}

**难度：★★★　状态：深度模板可用**

选择一个带`dsh-plugin`主题的社区项目，先证明其真实扩展形态，再固定源码和制品，完成能力图、服务端/客户端审查、权限与数据流、动态故障实验、升级和退出。结论使用五级证据状态，不能只写“推荐”。

详见 [`labs/lab05-plugin-review/REVIEW_TEMPLATE.md`](https://github.com/luxuzhou/dsh-in-depth/blob/main/labs/lab05-plugin-review/REVIEW_TEMPLATE.md)。

## Lab 06：扩展机制边界消融 {#lab-06}

**难度：★★★　状态：深度实验设计完成**

把同一个质量报告任务分别表达为 Skill、MCP、Workflow/Subagent 和确定性领域服务，固定输入与预算做消融，比较成功率、成本、权限面和错误相关性。

验收：不是“全部机制都用上”，而是用证据指出每种机制的净收益、必须保留的确定性边界和应删除的复杂度。

详见 [`labs/lab06-extension-boundaries/README.md`](https://github.com/luxuzhou/dsh-in-depth/tree/main/labs/lab06-extension-boundaries)。

## Lab 07：三种 Surface 契约对照 {#lab-07}

**难度：★★★　状态：深度实验设计完成**

用 Web、Headless 和 Python SDK 对同一只读仓库执行相同任务，比较有效配置、身份解析、Session 事件、审批/取消、恢复和最终证据；注入断连、重启、重复请求与越权恢复。

验收：核心语义一致，差异能够由 Surface 能力、Profile 或身份策略解释，并形成企业网关、多租户与外置状态的缺口清单。

详见 [`labs/lab07-surface-contracts/README.md`](https://github.com/luxuzhou/dsh-in-depth/tree/main/labs/lab07-surface-contracts)。

## 实验贡献规则

提交实验结果时，请记录操作系统、Node/Python版本、DSH提交、命令、退出码和产物摘要。包含模型调用时还要记录模型ID、提供商、时间和成本，但不得提交密钥或敏感业务数据。

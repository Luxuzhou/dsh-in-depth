# 配套实验

实验用于验证正文中的行为，不以“代码文件存在”代替真实运行证据。每个实验包含目标、前置条件、步骤、验收和延伸任务。

## Lab 01：源码地图与运行配置 {#lab-01}

**难度：★　状态：设计完成，待跨平台执行**

1. 克隆官方DSH并检出`upstream.lock.json`记录的提交。
2. 运行`dsh --profile web --dump-config`保存有效插件树。
3. 任选Tools、Skills或Session能力，找到Definition、Provider和Consumer。
4. 画出配置行、包、`ctx`服务键和模型可见工具之间的关系。

验收产物：`config-tree.txt`、一张Mermaid图和一页观察结论。禁止只提交目录截图。

详见 [`labs/lab01-source-map/README.md`](https://github.com/luxuzhou/dsh-in-depth/tree/main/labs/lab01-source-map)。

## Lab 02：可配置问候工具 {#lab-02}

**难度：★★　状态：代码完成，待在锁定DSH基线上实跑**

实现一个`greet`工具，验证参数Schema、配置默认值、工具调用、模型可见结果和插件热替换。基础代码位于`labs/lab02-greet-tool`。

验收：有效调用返回配置化问候；缺少`name`被Schema拒绝；非法配置在插件加载阶段失败；重载后工具没有重复注册。

## Lab 03：会话事件观察器 {#lab-03}

**难度：★★　状态：代码完成，待组合测试**

监听`session/event`，只输出事件序号、会话ID和类型，不记录用户正文和工具敏感结果。执行一次工具任务后，将事件序列与第3章生命周期图对照。

验收：每个打开的turn和step都有对应结束事件；工具call/result能够配对；观察器卸载后停止输出。

## Lab 04：受控 Data Agent {#lab-04}

**难度：★★★　状态：本地无依赖测试可运行**

用内存目录模拟“检验量”存在多种业务口径。系统必须先生成结构化状态和QueryPlan；存在歧义时拒绝执行；确认口径后签发绑定计划哈希的一次性审批；计划变化后旧审批失效。

运行：

```bash
python labs/lab04-governed-data-agent/test_mock_data_agent.py
```

## Lab 05：插件审查报告 {#lab-05}

**难度：★★　状态：模板可用**

选择一个带`dsh-plugin`主题的社区项目，按照来源、许可证、版本、安装脚本、权限、数据流、失败方式、测试、维护和退出十项形成证据表。结论只能是“进入观察区”“进入实验区”“受控试点”或“拒绝”，不能只写“推荐”。

详见`labs/lab05-plugin-review/REVIEW_TEMPLATE.md`。

## 实验贡献规则

提交实验结果时，请记录操作系统、Node/Python版本、DSH提交、命令、退出码和产物摘要。包含模型调用时还要记录模型ID、提供商、时间和成本，但不得提交密钥或敏感业务数据。

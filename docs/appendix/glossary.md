# 术语表

**Agent**：模型在Harness和环境中执行任务的运行主体。

**Harness**：组织上下文、工具、循环、状态与策略的运行系统。

**Cordis**：DSH底层插件框架，提供Context、Service、事件和生命周期。

**Plugin**：向Cordis Context注册能力或行为的运行模块。

**Capability Seam**：可替换能力的完整接缝，由Definition、Provider和Consumer构成。

**Bundle**：通过`dsh.bundle`声明交付Cordis配置层的安装包。

**Profile**：一套可启动装配，按顺序组合Bundle和用户覆盖。

**Turn**：从领取输入到不再欠工作的一轮，可包含多个Step。

**Step**：一次模型请求及该响应触发的工具执行。

**SessionEvent**：仅追加到会话日志、可用于回放的持久事实。

**Skill**：按需发现和加载的操作知识或SOP。

**MCP**：在进程或系统之间暴露工具、资源等能力的协议。

**QuerySpec**：Data Agent中的受控查询计划，描述指标、维度、过滤和排序，不包含自由SQL。

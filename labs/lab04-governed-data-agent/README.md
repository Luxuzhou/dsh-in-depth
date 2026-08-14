# Lab 04：受控 Data Agent

## 目标

这个无依赖教学模型不追求自然语言效果，只验证四个最小安全不变量：业务歧义未解决前不能规划；计划具有稳定哈希；审批绑定用户和计划；审批只能消费一次。

```bash
python labs/lab04-governed-data-agent/test_mock_data_agent.py
```

预期三个测试通过。阅读 `mock_data_agent.py`，画出 `ConversationState → QueryPlan → Approval → Result` 状态图，说明每个检查位于哪一条信任边界。

## 深度扩展

按顺序增加以下测试，每一步先写失败用例：

1. 审批绑定 `tenant_id`、`conversation_id`、状态版本和有效期；
2. QueryPlan 规范化序列化，过滤顺序不影响哈希、值变化必须影响哈希；
3. 状态字段记录来源轮次，支持 ADD/REPLACE/REMOVE；
4. 乐观锁拒绝基于旧版本提交的状态补丁；
5. 权限或语义版本变化后旧审批失效；
6. 并发消费同一审批时仅一次成功；
7. 区分合法空集、超时、部分数据和权限过滤为空；
8. 把内存目录替换为 HTTP 语义服务，并注入断网、慢响应和畸形结果。

## 对照实验

另写一个只读 `execute_sql(sql)` 版本，使用同一组歧义、越权、高成本和提示注入案例。比较两种方案的错误执行空间，而不是比较哪一个 Demo 回答更流畅。

## 交付证据

提交测试输出、QuerySpec/Plan Schema、审批字段、失败矩阵和一条三轮对话轨迹。不得把本实验结果称为生产可用 Data Agent；完成语义治理、真实权限、数据质量和端到端金标准后才能进入试点。

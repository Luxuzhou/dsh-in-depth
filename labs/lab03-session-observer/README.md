# Lab 03：会话事件观察器

## 目标

验证 Agent 的 Turn/Step 嵌套、工具 continuation、取消收敛和 Session 投影，并证明“Agent idle”不是可靠的消息回执。

## 数据约定

观察器只记录序号、时间、Session/Agent/Turn/Step/Call 标识、事件类型和结束原因；不记录用户正文、系统提示、工具参数与结果。实验只使用合成任务。

## 基础装载

通过 `--patch` 把 `index.ts` 插入锁定版本的 Web Profile，保存有效配置。先运行一个明确要求调用只读工具的任务，将终端序列和第 3 章生命周期图对照。

## 四条必测轨迹

1. 无工具、自然完成；
2. 一次工具调用后 continuation；
3. pre-step 因缺少输入而拒绝；
4. 工具运行期间主动取消。

每条轨迹检查 Turn 是否恰好开放/结束一次、Step 是否正确嵌套、call/result 是否配对、结束原因和 Agent status 是否一致。取消实验还要等待外部资源停止，不能把收到 AbortSignal 当作完成。

## 投影与崩溃练习

根据事件构建两个纯函数投影：当前 Agent 状态；每个工具调用的终态。制造重复事件和进程在 call 后/result 前崩溃的前缀，验证投影幂等并把未闭合调用标为 `unknown/interrupted`，而不是伪造成功。

反事实：错误地把 `agent/status=idle` 当作某条消息的回执，连续排入两个 followup，记录无法可靠配对的原因；再用 message ID、claimed 事件和 Turn 边界修正。

## 验收与清理

观察器卸载后必须停止输出；三次重载不能增加重复监听器；日志中不得出现合成正文。提交事件字段字典、四条轨迹、投影断言、反事实分析和隐私说明。

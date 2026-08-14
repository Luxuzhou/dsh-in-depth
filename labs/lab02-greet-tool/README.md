# Lab 02：可配置问候工具

## 目标

用最小插件验证第 2、5、6 章的五个不变量：配置先校验；模型只看到注册后的 Schema；执行返回规范 ContentBlock；注册随 Fiber 卸载；Bundle/Profile 组合可以重放。

## 前置条件

- DSH `47f943859bef60e4160492346772ded9b24f765a`；
- 与该提交匹配的 Node/pnpm 环境；
- 独立测试 Profile，不复用生产 Home；
- 合成名称，不提交模型密钥。

## 阶段一：overlay 装载

把下面配置中的路径替换为本仓库 `index.js` 的绝对路径：

```yaml
- insert:
    - id: book-greet-local
      name: '/absolute/path/to/dsh-in-depth/labs/lab02-greet-tool/index.js'
      config:
        greeting: '你好'
```

```bash
pnpm dsh web --patch /absolute/path/to/overlay.yml
```

保存 `--dump-config` 输出，确认生效行来自 overlay。向 Agent 发送“请使用 greet 工具问候 Ada”，保存工具 call/result 事件而非只保存最终回复。

## 阶段二：反事实与生命周期

依次执行：缺少 `name`；传入额外字段；把 `greeting` 改为非法配置；修改问候语触发重载；连续重载三次；卸载插件后再次要求调用。每次先写预期，再记录真实状态、工具 Schema 数量和事件。

验收条件：有效调用返回配置化问候；非法参数在执行前拒绝；非法配置不替换最后一个可用实例；重载后只有一个同名工具；卸载后工具不可见且无重复监听器。

## 阶段三：Bundle 与 Profile

按第 6 章补全包 manifest 和 patch，在全新测试 Profile 安装；保存 lockfile、有效配置和制品摘要；用 Profile patch 覆盖配置，再移除 Bundle，验证配置行和依赖都撤销。

## 交付证据

- 环境与上游提交；
- overlay、Bundle 和最终 Profile 配置；
- 正常、拒绝、重载、卸载四类事件摘要；
- 预测/实际对照表；
- 一段生产边界结论：哪些行为由 DSH 保证，哪些仍需企业控制。

# Lab 01：源码地图与运行配置

## 目标

从“实际启动的插件树”反向定位源码，而不是浏览全部七千多个文件。

## 步骤

```bash
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
git checkout 47f943859bef60e4160492346772ded9b24f765a
pnpm install
pnpm run build
pnpm dsh --profile web --dump-config > config-tree.txt
```

选择配置中的一个工具行，依次记录：Bundle来源、patch行ID、插件包、注入服务、`ctx`键、工具名和相关会话事件。

## 验收模板

```markdown
# <能力名> 源码地图

- DSH提交：
- 配置行ID：
- Bundle：
- Service Definition：
- Provider：
- Consumer：
- 模型可见接口：
- 持久事件：
- 实时事件：
- 可替换点：
- 观察到的限制：
```

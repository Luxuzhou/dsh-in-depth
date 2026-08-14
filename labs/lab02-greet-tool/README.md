# Lab 02：可配置问候工具

本例与书籍上游锁定版本一致。建议先在官方源码仓库中通过绝对路径overlay加载，观察成功后再练习Bundle安装。

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

向Agent发送：“请使用greet工具问候Ada。”随后修改`greeting`并验证插件热替换。

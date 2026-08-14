# 贡献指南

本仓库把书籍视为可验证的软件项目。修改正文、实验或上游基线时，请遵循以下约定。

## 内容类型

写作时尽量标明事实的来源层级：

- **官方保证**：官方 README、文档或公开接口明确承诺的行为。
- **源码观察**：在锁定提交中看到的实现，未来可能变化。
- **社区实践**：第三方插件采用的方法，不代表官方推荐。
- **工程建议**：本书基于风险和可维护性给出的判断。

## 章节模板

每章至少包含：学习目标、核心问题、正文、源码路标、配套实验、本章小结、思考题、求职面试题。新增 API 说明时必须链接到固定提交，而不是只链接 `master`。

## 更新上游基线

1. 修改 `upstream.lock.json`。
2. 检查官方 README、架构、Agent 生命周期、工具、会话、插件开发和发布文档。
3. 运行 `python scripts/check_upstream.py --local-only`。
4. 更新 `docs/appendix/compatibility.md`，说明新增、删除和破坏性变化。
5. 重新执行受影响实验并更新 `docs/LAB_STATUS.md`。
6. 在 `CHANGELOG.md` 中记录书籍版本。

## 提交前检查

```bash
python scripts/check_content.py
uv sync --extra docs
uv run mkdocs build --strict
python scripts/export_book.py
```

不要提交 API Key、数据库口令、患者信息或真实生产数据。

$ErrorActionPreference = 'Stop'

uv sync --locked --extra docs
uv run python scripts/check_content.py
uv run mkdocs build --strict
uv run ghp-import -n -p -f site

Write-Host 'Published https://luxuzhou.github.io/dsh-in-depth/'

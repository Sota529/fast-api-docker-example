# FastAPI Docker Example

## プロジェクト概要
FastAPI + MySQL + Docker 構成のサンプルプロジェクト。Python 3.13 使用。

## 開発コマンド

```bash
# 起動
docker compose up -d

# 停止
docker compose down

# lint
uv run ruff check app/

# format
uv run ruff format app/
```

## プロジェクト構造

```
app/
├── main.py        # FastAPIインスタンス + router登録
├── database.py    # DB接続
├── routers/       # エンドポイント
├── models/        # SQLAlchemyモデル
└── schemas/       # Pydanticスキーマ
```

## コーディング規約

- ruff による lint/format（line-length=88）
- 新機能追加時は routers/, models/, schemas/ にファイル追加

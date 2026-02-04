# FastAPI Docker Example

FastAPI を Docker で動かすサンプルプロジェクトです。

## 必要なもの

- [uv](https://docs.astral.sh/uv/)（パッケージ追加時のみ）
- Docker

## 機能

- FastAPI による REST API
- SQLAlchemy ORM による MySQL データベース連携
- Docker Compose による開発環境の構築

## uv のセットアップ

パッケージの追加・更新時に必要です。

### インストール

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# または Homebrew
brew install uv
```

### パッケージの追加

```bash
# パッケージ追加
uv add httpx

# 開発用パッケージ追加
uv add --dev pytest

# Docker に反映
docker compose up --build
```

## ローカル開発

```bash
docker compose up
```

http://localhost:8000 でアクセスできます。コード変更が自動反映されます。

### データベース

- MySQL 8.0 がコンテナで起動します
- アプリケーション起動時に自動的にテーブルが作成されます
- サンプルデータが自動的に投入されます

## API エンドポイント

http://localhost:8000/docs で確認できます。

### 利用可能なエンドポイント

- `GET /` - Hello World
- `GET /health` - ヘルスチェック
- `GET /users` - ユーザー一覧取得（ORM経由でDBから取得）
- `GET /users/{user_id}` - 特定ユーザーの取得
- `POST /users` - 新規ユーザーの作成

## リリースフロー

```
feature/* → develop → main
              ↓         ↓
            STG       PRD
```

### 開発 → ステージング

1. `feature/*` ブランチで開発
2. `develop` へ PR を作成・マージ
3. **STG に自動デプロイ**

### ステージング → 本番

1. `develop` → `main` へ PR を作成（手動）
2. PR をマージ
3. **PRD に自動デプロイ**

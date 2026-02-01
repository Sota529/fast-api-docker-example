# FastAPI Docker Example

FastAPI を Docker で動かすサンプルプロジェクトです。

## 必要なもの

- [uv](https://docs.astral.sh/uv/)（パッケージ追加時のみ）
- Docker

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

## API エンドポイント

http://localhost:8000/docs で確認できます。

## リリースフロー

### 開発からステージングへ

- `develop` ブランチにマージされると、ステージング環境（stg）にデプロイされます
- GitHub Actions: `.github/workflows/deploy-stg.yml`
- また、`develop` ブランチへのプッシュ時に、`main` ブランチへのリリース PR が自動作成されます（`.github/workflows/create-release-pr.yml`）

### ステージングから本番へ

- `main` ブランチにマージされると、本番環境（prd）にデプロイされます
- GitHub Actions: `.github/workflows/deploy-prd.yml`
- **重要**: `main` ブランチへは、自動生成されたリリース PR 経由でのみマージしてください

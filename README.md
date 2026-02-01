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

このプロジェクトでは、ブランチベースの自動デプロイフローを採用しています。

### ステージング環境へのリリース

- `develop` ブランチにマージされると、ステージング環境（stg）にデプロイされます
- GitHub Actions ワークフロー: `.github/workflows/deploy-stg.yml`
- 自動的に以下の処理が実行されます：
  - Docker イメージのビルド
  - Amazon ECR へのプッシュ
  - Amazon ECS ステージング環境へのデプロイ

### 本番環境へのリリース

- `main` ブランチにマージされると、本番環境（prd）にデプロイされます
- GitHub Actions ワークフロー: `.github/workflows/deploy-prd.yml`
- 自動的に以下の処理が実行されます：
  - Docker イメージのビルド
  - Amazon ECR へのプッシュ
  - Amazon ECS 本番環境へのデプロイ

### リリース PR の自動作成

- `develop` ブランチへのプッシュ時に、`main` ブランチへのリリース PR が自動作成されます
- GitHub Actions ワークフロー: `.github/workflows/create-release-pr.yml`
- PR には develop と main の差分コミット一覧が含まれます
- 既に PR が存在する場合は、内容が更新されます

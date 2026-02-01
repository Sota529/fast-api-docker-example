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

### 開発からステージングへ

1. **機能ブランチから `develop` へのマージ**
   - プルリクエストを作成し、レビュー後に `develop` ブランチにマージします

2. **ステージング環境への自動デプロイ**
   - `develop` ブランチへのマージ時に、ステージング環境（stg）へ自動デプロイされます
   - 使用される GitHub Actions: `.github/workflows/deploy-stg.yml`
   - 実行される処理：
     - Docker イメージのビルド
     - Amazon ECR へのプッシュ
     - Amazon ECS ステージング環境へのデプロイ

3. **リリース PR の自動作成**
   - `develop` ブランチへのプッシュ時に、`main` ブランチへのリリース PR が自動作成されます
   - 使用される GitHub Actions: `.github/workflows/create-release-pr.yml`
   - PR には `develop` と `main` の差分コミット一覧が含まれます
   - 既に PR が存在する場合は、内容が自動更新されます

### ステージングから本番へ

1. **リリース PR のマージ**
   - ステージング環境での動作確認後、自動作成されたリリース PR を `main` ブランチにマージします
   - **重要**: `main` ブランチへの直接プッシュは行わず、必ずリリース PR 経由でマージしてください

2. **本番環境への自動デプロイ**
   - `main` ブランチへのマージ時に、本番環境（prd）へ自動デプロイされます
   - 使用される GitHub Actions: `.github/workflows/deploy-prd.yml`
   - 実行される処理：
     - Docker イメージのビルド
     - Amazon ECR へのプッシュ
     - Amazon ECS 本番環境へのデプロイ

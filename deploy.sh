#!/bin/bash

# === 사용자 정보 설정 ===
GITHUB_USERNAME="rentgist"
REPO_NAME="slowhouse-clone"
TARGET_BRANCH="main"
BUILD_DIR="slowhouse_clone"

# === GitHub 원격 저장소 URL (HTTPS 방식) ===
REPO_URL="https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"

# === 배포 시작 ===
cd "$BUILD_DIR" || { echo "❌ 디렉토리 이동 실패"; exit 1; }

echo "📦 Git 초기화 중..."
git init
git branch -M $TARGET_BRANCH
git remote add origin "$REPO_URL"

echo "📤 파일 커밋 및 GitHub에 푸시..."
git add .
git commit -m "Deploy site to GitHub Pages"
git push -u origin $TARGET_BRANCH

echo "✅ 완료! 사이트 확인 👉 https://$GITHUB_USERNAME.github.io/$REPO_NAME/"

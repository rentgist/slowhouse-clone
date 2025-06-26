import os
import requests

# 누락된 상대 경로 리스트
missing_paths = [
    "static/common/img/sp_common.png",
    "static/common/img/sp_pc_3097db.png",
    "static/front/img/board_ico_arrow.png",
    "static/front/img/dot_line_pc.gif",
    "static/front/img/font/modoo_20b606.svg",
]

# 원본 기준 URL
base_url = "https://slowhousegj.modoo.at/"
clone_root = "slowhouse_clone"  # 압축 해제한 루트 폴더명

# 다운로드 함수
def download_missing_files():
    for path in missing_paths:
        url = base_url + path
        save_path = os.path.join(clone_root, path)

        # 디렉토리 먼저 생성
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        try:
            print(f"Downloading {url}")
            res = requests.get(url, timeout=10)
            res.raise_for_status()
            with open(save_path, "wb") as f:
                f.write(res.content)
            print(f"[✔] Saved to {save_path}")
        except Exception as e:
            print(f"[✘] Failed to download {url}: {e}")

# 실행
download_missing_files()

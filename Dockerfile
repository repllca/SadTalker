# ベースイメージ（SadTalker公式）
FROM wawa9000/sadtalker

# 必要パッケージ
RUN apt-get update && apt-get install -y git ffmpeg && rm -rf /var/lib/apt/lists/*

# pip アップデート
RUN pip install --upgrade pip

# FastAPI + uvicorn をインストール
RUN pip install --no-cache-dir fastapi uvicorn
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir fastapi uvicorn python-multipart
# 作業ディレクトリ
WORKDIR /SadTalker_copy

# ソースコードをコピー
COPY . .

# ポートを公開
EXPOSE 8000

# コンテナ起動時に FastAPI を起動
ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

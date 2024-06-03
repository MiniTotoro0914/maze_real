# app/Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir \
	-r requirements.txt

# RUN apt-get update && apt-get install antiword

# 資材ファイルのコピー
COPY ./settings /app/settings
COPY ./src /app/src

# baseディレクトリを作業ディレクトリに設定
WORKDIR /app/src

# アプリケーションの実行 確認用
CMD ["/bin/bash", "-c", "ls /app/src"]
# 実際必要なのはこっち
# CMD ["python", "test_base_01.py"]
CMD ["python", "./py/access_pic.py"]

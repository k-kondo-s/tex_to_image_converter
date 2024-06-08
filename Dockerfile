FROM texlive/texlive:latest

# 必要なパッケージのインストール
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

# 仮想環境の作成
RUN python3 -m venv /venv

# 仮想環境のアクティベート
ENV PATH="/venv/bin:$PATH"

# Gradio と必要な Python パッケージのインストール
RUN pip install --no-cache-dir gradio

# 作業ディレクトリの設定
WORKDIR /app

# TeX から画像を生成するスクリプトをコピー
COPY generate_image.py .

# ポート番号の公開
EXPOSE 7860

# Gradio アプリケーションの起動
CMD ["python", "generate_image.py"]

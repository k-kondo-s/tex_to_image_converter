# Tex To Image Converter

Tex To Image Converter は、TeX のソースコードを画像に変換するツールです。以下の2つの方法で使用できます。

## 方法1: シンプルな変換

単純に TeX のソースコードを画像に変換したい場合は、以下の手順を実行してください。

1. `formula.tex` ファイルを準備します。このファイルに TeX のソースコードを記述してください。

2. 以下のコマンドを実行します：

   ```
   docker run --rm -it -v $PWD:/workdir texlive/texlive sh -c "platex formula.tex && dvipng -D 3000 -bg Transparent -T tight -o formula.png formula.dvi && latexmk -c"
   ```

   このコマンドは、`formula.tex` ファイルをコンパイルし、`formula.png` という名前の画像ファイルを生成します。

## 方法2: Gradio を使った変換

Docker と Gradio を使って、インタラクティブに TeX のソースコードを画像に変換することもできます。以下の手順を実行してください。

### イメージをビルドする

1. このリポジトリをクローンまたはダウンロードします。

2. リポジトリのルートディレクトリに移動し、以下のコマンドを実行してDockerイメージをビルドします：

   ```
   docker build --no-cache -t kenchaaan/texlive-gradio .
   ```

### コンテナの起動

1. ビルドまたはプルしたイメージを使って、以下のコマンドでDockerコンテナを起動します：

   ```
   docker run --rm -d -p 7860:7860 --name texlive-gradio-app kenchaaan/texlive-gradio
   ```

2. コンテナが起動したら、ブラウザで `http://localhost:7860` にアクセスします。

3. Gradio のインターフェースが表示されます。TeX のソースコードを入力し、"Submit" ボタンをクリックすると、画像が生成されます。

コンテナのログを確認するには、以下のコマンドを実行します：

```
docker logs -f texlive-gradio-app
```

これで、Tex To Image Converter を使って TeX のソースコードを画像に変換できます。シンプルな変換とGradioを使った変換の2つの方法から選んでください。

Docker Hub からイメージをプルする方法を追加したので、自分でイメージをビルドしなくても、公開されているイメージを使ってすぐにコンテナを起動できます。

### 全部のコマンド

```
docker stop texlive-gradio-app \\
docker build --no-cache -t kenchaaan/texlive-gradio . && docker run --rm -d -p 7860:7860 --name texlive-gradio-app kenchaaan/texlive-gradio
```
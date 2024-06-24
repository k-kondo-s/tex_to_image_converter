import os
import tempfile
import subprocess
import gradio as gr


def generate_image(tex_code):
    # テンプレートの定義
    template = r"""
    \documentclass[dvipdfmx]{{jsarticle}}
    \usepackage{{amsmath,amssymb}}
    \begin{{document}}
    \pagestyle{{empty}}
    {}
    \end{{document}}
    """

    # 一時ディレクトリの作成
    temp_dir = tempfile.mkdtemp(prefix="tex_")

    # TeX ファイルのパス
    tex_file = os.path.join(temp_dir, "formula.tex")

    # tex_code の空行を削除
    tex_code = "\n".join([line for line in tex_code.split("\n") if line.strip()])

    # TeX ソースコードをテンプレートに埋め込む
    tex_source = template.format(tex_code)

    # TeX ソースコードを一時ファイルに保存
    with open(tex_file, "w") as file:
        file.write(tex_source)

    # platex を使用して TeX ファイルをコンパイル
    subprocess.run(["platex", "-output-directory", temp_dir, tex_file], check=True)

    # dvipng を使用して DVI ファイルを PNG 画像に変換
    dvi_file = os.path.join(temp_dir, "formula.dvi")
    png_file = os.path.join(temp_dir, "formula.png")
    subprocess.run(
        [
            "dvipng",
            "-D",
            "3000",
            "-bg",
            "Transparent",
            "-T",
            "tight",
            "-o",
            png_file,
            dvi_file,
        ],
        check=True,
    )

    # 生成された画像のパスを返す
    return png_file


# Gradio インターフェースの作成
iface = gr.Interface(
    fn=generate_image,
    inputs=[
        gr.Textbox(label="TeX のソースコード. Shift + Enter で改行."),
    ],
    outputs=gr.Image(type="filepath"),
    title="TeX to Image Converter",
    description="TeX のソースコードを画像に変換します.",
)

# Gradio アプリケーションの起動
if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)

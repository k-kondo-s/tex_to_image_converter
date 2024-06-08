docker run --rm -it -v $PWD:/workdir texlive/texlive sh -c "platex formula.tex && dvipng -D 3000 -bg Transparent -T tight -o formula.png formula.dvi && latexmk -c"




docker build --no-cache -t texlive-gradio .
docker run --rm -d -p 7860:7860 --name texlive-gradio-app texlive-gradio
docker logs -f texlive-gradio-app


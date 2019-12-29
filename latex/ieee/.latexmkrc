$do_cd = 1;
$pdf_mode = 1;
$bibtex_use = 2;
$out_dir = "../build";
@default_files = ('src/main.tex');
$pdflatex = "pdflatex --shell-escape %O %S";
$pdf_previewer = "start open -a preview %O %S";

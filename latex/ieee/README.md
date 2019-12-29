# LaTeX

This little subproject helps writing LaTeX-papers.
It has several features, like

* execute `latexmk` in root-folder to build and everything's fine due to `.latexmkrc`.
* execute `latexmk -c` to clean.

The folder structure looks like:

```zsh
LaTeX-root
├── README.md
├── build
│   ├── main.pdf
│   └── ...
├── custom                  # should be added to .gitignore
│   └── IEEEtran_HOWTO.pdf
├── res
│   └── graphics
│       └── fig1.png
├── scripts
│   └── gitignore.sh        # sh scripts/.gitignore > .gitignore
└── src
    ├── IEEEtran.cls
    ├── bibliography.bib
    ├── content
    │   ├── abbreviations.tex
    │   ├── abstract.tex
    │   ├── acknowledgement.tex
    │   ├── ease_of_use.tex
    │   ├── introduction.tex
    │   ├── prepare_your_paper_before_styling.tex
    │   └── references.tex
    ├── main.tex
    └── preamble
        └── pkgs_and_options.tex

```

## Copyright

The underlying IEEE-template has been downloaded from [www.ieee.org][www_ieee_org] in `July 4th, 2019` and is from `July 2018`.
Made changes are just structure-, not content-related:

* The IEEE-template itself has been splitted into several files.
* Its bibliography-examples has been changed slightly.
* Indentions and a `graphicspath` were added.
* The LaTeX-code has been refactored such that every line contains at most one sentence.
  This helps a lot (especially, but not only, when using `vim`).

[www_ieee_org]: https://www.ieee.org/conferences/publishing/templates.html

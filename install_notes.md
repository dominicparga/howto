# Installation notes

## Overview

The following table shows all tools in this file and whether a tool is explained here (:ballot_box_with_check:), not explained here but available (:black_square_button:) or not available at all (:heavy_multiplication_x:).

If some tool is not mentioned in an own section, but is marked in the table as explained, it can be installed easily via the respective package-manager (`brew`/`brew cask` in `macOS`, `apt` in `ubuntu`, ...).

| tools                             | `macOS`                 |
|:----------------------------------|:-----------------------:|
| [`Alfred`](#alfred)               | :ballot_box_with_check: |
| [`Bash`](#bash)                   | :ballot_box_with_check: |
| `GNU coreutils`                   | :ballot_box_with_check: |
| `Discord`                         | :ballot_box_with_check: |
| `Dropbox`                         | :ballot_box_with_check: |
| `Enpass`                          | :ballot_box_with_check: |
| `Firefox`                         | :ballot_box_with_check: |
| `gimp`                            | :ballot_box_with_check: |
| `git`                             | :ballot_box_with_check: |
| `grep`                            | :ballot_box_with_check: |
| [`Homebrew`](#brew)               | :ballot_box_with_check: |
| `htop`                            | :ballot_box_with_check: |
| [`Java` and `Scala`](#java-scala) | :ballot_box_with_check: |
| `LaTex`                           | :ballot_box_with_check: |
| `Microsoft-Office`                | :ballot_box_with_check: |
| `musescore`                       | :ballot_box_with_check: |
| `neovim`                          | :ballot_box_with_check: |
| `node`                            | :ballot_box_with_check: |
| [`python`](#python)               | :ballot_box_with_check: |
| `spotify`                         | :ballot_box_with_check: |
| `teamspeak`                       | :ballot_box_with_check: |
| `Telegram`                        | :ballot_box_with_check: |
| `tree`                            | :ballot_box_with_check: |
| [`VisualStudioCode`](#vscode)     | :ballot_box_with_check: |
| `vlc`                             | :ballot_box_with_check: |
| `zsh`                             | :ballot_box_with_check: |
| [`Heroku CLI`](#heroku)           | :ballot_box_with_check: |
| `virtualbox`                      | :ballot_box_with_check: |
| `teamviewer`                      | :ballot_box_with_check: |

## Alfred <a name="alfred"></a>

A very intelligent and handy search-bar replacing `macOS`'s `spotlight`

### macOS

```zsh
brew cask install alfred
```

You may add Web-Search-functionality for translating.
Calling `Alfred` and entering

```text
ger hello
engl Hallo
```

should open the respective translation page in google-translator.
The Web-Search-setting looks like this:

- Search-URL: `https://translate.google.com/#from/to/{query}`,  
  e.g. `https://translate.google.com/#en/de/{query}`
- Title: `From -> To: {query}`

## Bash <a name="bash"></a>

On `Linux`, it's up-to-date, but `macOS` uses old versions due to license-issues.

### macOS

```zsh
brew install bash
brew install bash-completion@2
```

## Homebrew <a name="brew"></a>

### macOS

Package-manager for `macOS`.
The other installation-guides (if `macOS`) bases on `brew`.
I prefer it over `macports` since, a few years ago, installing compiler for `c++` was difficult in `macports`.
Further, `brew` supports a lot of software.

```zsh
if ( command -v brew 1>/dev/null 2>/dev/null ); then
    echo "Updating homebrew and formulae..."
    brew update
    brew upgrade
    brew cask upgrade
    brew cleanup
else
    echo "Installing homebrew..."
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi
```

## Java and Scala <a name="java-scala"></a>

### macOS

```zsh
# important execution order!
brew cask install java
brew install scala
brew install sbt
```

## LaTeX <a name="latex"></a>

### macOS

```zsh
brew cask install mactex
```

## python <a name="python"></a>

### general

TODO

### macOS

```zsh
brew install python
brew install python@2
```

## VisualStudioCode <a name="vscode"></a>

### macOS

```zsh
brew cask install visual-studio-code
```

### ubuntu

TODO not installable via apt?

## Heroku <a name="heroku"></a>

### macOS

```zsh
brew install heroku/brew/heroku
```

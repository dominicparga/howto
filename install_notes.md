# Installation notes

## Overview

The following table shows all tools in this file and whether a tool is available and explained here (:ballot_box_with_check:), not explained here but maybe available (:black_square_button:) or, for sure, not available at all (:heavy_multiplication_x:).

If some tool is not mentioned in an own section, but is marked in the table as explained, it can be installed easily via the respective package-manager (`brew`/`brew cask` in `macOS`, `apt` in `ubuntu`, ...) or is installed per default.

| tools                             | `macOS`                  | `ubuntu`                 |
|:----------------------------------|:------------------------:|:------------------------:|
| [`Alfred`](#alfred)               | :ballot_box_with_check:  | :black_square_button:    |
| [`Bash`](#bash)                   | :ballot_box_with_check:  | :ballot_box_with_check:  |
| `GNU coreutils`                   | :ballot_box_with_check:  | :ballot_box_with_check:  |
| `Discord`                         | :ballot_box_with_check:  | :black_square_button:    |
| `Dropbox`                         | :ballot_box_with_check:  | :black_square_button:    |
| `Enpass`                          | :ballot_box_with_check:  | :black_square_button:    |
| `Firefox`                         | :ballot_box_with_check:  | :black_square_button:    |
| `gimp`                            | :ballot_box_with_check:  | :black_square_button:    |
| `git`                             | :ballot_box_with_check:  | :ballot_box_with_check:  |
| `grep`                            | :ballot_box_with_check:  | :ballot_box_with_check:  |
| [`Homebrew`](#brew)               | :ballot_box_with_check:  | :heavy_multiplication_x: |
| `htop`                            | :ballot_box_with_check:  | :ballot_box_with_check:  |
| [`Java` and `Scala`](#java-scala) | :ballot_box_with_check:  | :black_square_button:    |
| `LaTex`                           | :ballot_box_with_check:  | :black_square_button:    |
| `Microsoft-Office`                | :ballot_box_with_check:  | :black_square_button:    |
| `musescore`                       | :ballot_box_with_check:  | :black_square_button:    |
| `neovim`                          | :ballot_box_with_check:  | :ballot_box_with_check:  |
| `node`                            | :ballot_box_with_check:  | :black_square_button:    |
| [`Nord`](#nord) (color-scheme)    | :ballot_box_with_check:  | :ballot_box_with_check:  |
| [`npm`](#npm)                     | :ballot_box_with_check:  | :ballot_box_with_check:  |
| [`python`](#python)               | :ballot_box_with_check:  | :ballot_box_with_check:  |
| [`rust`](#rust)                   | :ballot_box_with_check:  | :ballot_box_with_check:  |
| `spotify`                         | :ballot_box_with_check:  | :black_square_button:    |
| `teamspeak`                       | :ballot_box_with_check:  | :black_square_button:    |
| `Telegram`                        | :ballot_box_with_check:  | :black_square_button:    |
| `tree`                            | :ballot_box_with_check:  | :ballot_box_with_check:  |
| [`VisualStudioCode`](#vscode)     | :ballot_box_with_check:  | :ballot_box_with_check:  |
| `vlc`                             | :ballot_box_with_check:  | :black_square_button:    |
| `zsh`                             | :ballot_box_with_check:  | :ballot_box_with_check:  |
| [`Heroku CLI`](#heroku)           | :ballot_box_with_check:  | :black_square_button:    |
| `virtualbox`                      | :ballot_box_with_check:  | :black_square_button:    |
| `teamviewer`                      | :ballot_box_with_check:  | :black_square_button:    |

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

### ubuntu

```zsh
# important execution order!
sudo apt-get install -y openjdk-11-jdk
sudo apt-get install -y scala
```

## LaTeX <a name="latex"></a>

### macOS

```zsh
brew cask install mactex
```

## Nord (color-scheme) <a name="nord"></a>

This dark-scheme is light and pretty and available for all kind of software.
All documentation can be found on their [homepage](https://www.nordtheme.com/) or the respective [GitHub-repo](https://github.com/arcticicestudio/nord).

## npm <a name="npm"></a>

### ubuntu

Since installing on `Ubuntu 18.04` could fail, the following code snippets helps with installation.

```zsh
# since installing on Ubuntu 18.04 could fail

# NOTE
# PATH in shellrc.sh is related to ${npm_version} and ${npm_distro}

npm_version='v11.10.0'
npm_distro='linux-x64'

dest_dir="/usr/local/lib/nodejs"


sudo mkdir -p "${dest_dir}"
wget -c https://nodejs.org/download/release/latest/node-${npm_version}-${npm_distro}.tar.xz -O - | sudo tar -xJv -C "${dest_dir}"
```

Don't forget to update `${PATH}`.

```zsh
export PATH="/usr/local/lib/nodejs/node-${npm_version}-${npm_distro}/bin:${PATH}"
```

## python <a name="python"></a>

### general

After installing python, these packages are helpful.

```zsh
_pip_packages=(
    autopep8
    docopt
    matplotlib
    numpy
    pip
    pipenv
    pylint
    setuptools
)
for _item in ${_pip_packages[@]}; do
    python3 -m pip install -U ${_item}
    python2 -m pip install -U ${_item}
    echo
done
```

### macOS

```zsh
brew install python
brew install python@2
```

### ubuntu

```zsh
sudo apt-get install -y python3
sudo apt-get install -y python
```

## Rust <a name="rust"></a>

Just take a look at [the homepage](https://www.rust-lang.org/tools/install).

Keep in mind that updating `rustup` is needed, e.g. for the compiler `rustc`, since `brew` for instance (`macOS`) has `rust` as `formulae`.

## VisualStudioCode <a name="vscode"></a>

### extensions

Handy extensions can be found in [these dotfiles](https://github.com/dominicparga/dotfiles)

### macOS

```zsh
brew cask install visual-studio-code
```

### ubuntu

See [vscode-docs](https://code.visualstudio.com/docs/setup/linux)

## Heroku <a name="heroku"></a>

### macOS

```zsh
brew install heroku/brew/heroku
```

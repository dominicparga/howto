# Installation notes

## Overview

The following table shows all tools in this file and whether a tool is explained here (:ballot_box_with_check:), not explained here but available (:black_square_button:) or not available at all (:heavy_multiplication_x:).

| tools                         | `macOS`                 |
|-------------------------------|-------------------------|
| [`alfred`](#alfred)           | :ballot_box_with_check: |
| [`brew`](#brew)               | :ballot_box_with_check: |
| [Java and Scala](#java-scala) | :ballot_box_with_check: |

## Alfred <a name="alfred"></a>

A very intelligent and handy search-bar for `macOS`

```zsh
brew cask install alfred
```

## Homebrew <a name="brew"></a>

Package-manager for `macOS`.
The other installation-guides (if `macOS`) bases on `brew`.
I prefer it over `macports` since, a few years ago, installing compiler for c++ was difficult.
Further, it supports a lot of software.

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

```zsh
# important execution order!
brew cask install java
brew install scala
brew install sbt
```

## TODO

```zsh
################################################################################
# define and install formulae

# unordinary formulae in alphabetical order
brew install bash
brew install bash-completion@2
brew cask install mactex
brew install coreutils
brew cask install discord
brew cask install dropbox
brew cask install enpass
brew cask install firefox
brew cask install gimp
brew install git
brew install grep
brew install htop
brew cask install microsoft-office
brew cask install musescore
brew install neovim
brew install node
brew install python
brew install python@2
brew cask install spotify
brew cask install teamspeak-client
brew cask install Telegram
brew install tree
brew cask install visual-studio-code
brew cask install vlc
brew install zsh
brew install heroku/brew/heroku

# needs extra stuff
brew cask install virtualbox
brew cask install teamviewer # needs password
```

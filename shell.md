# Shell

The following conventions and suggestions should be followed.
They help a lot keeping overview and the code clear.

Although the language is bash or zsh, the project's style bases on python's philosophie.

[`The Zen of Python`][www_wikipedia_zen_of_python] should be kept in mind while coding.
From [Wikipedia - Python][www_wikipedia_python]:  
In general, the language's core philosophy (...) includes

```text
Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Readability counts.
```

which may be called `pythonic`.

## Table of Contents <a name="toc"></a>

1. [File Style](#file-style)
1. [Coding Conventions](#coding-conventions)
1. [Documentation](#documentation)
1. [Project Conventions](#project-conventions)
1. [Colors](#colors)

## File Style <a name="file-style"></a>

* Maximum line width is `80`.
  Exceptions can be made for String-constants and similar.

  _Humans have trouble reading the code with increasing line width.
  In general, more than `80` is not recommended._

* Use `4 spaces` for indention (p.s.: [could help salary](https://stackoverflow.blog/2017/06/15/developers-use-spaces-make-money-use-tabs)!).

## Coding Conventions <a name="coding-conventions"></a>

First of all, a great linter [`shellcheck`][www_github_koalaman_shellcheck] helps distinguishing between styles/standards like `POSIX`, `bash`.

* Functions, fields and file names are written in `snake_case`.

  Since functions and fields are added to the shell's environment, their names are slightly changed to prevent conflicts or verbose autocompletion and help understanding the code:
  * exported ("public") fields' names are written in `UPPER_CASE_SNAKE_CASE`
  * private fields' names are written in `__UPPER_CASE_SNAKE_CASE` (double-underscore!)
  * public functions' names are written in `snake_case`
  * private functions' names are written in `__snake_case` (double-underscore)

  ```zsh
  # BAD
  Greet() {
      used_shell="unknown"
      # ...
  }

  export dotfiles="..."



  # GOOD
  __finished() {
      echo "Finished"
  }

  # used in the shell, hence no leading dunderscore
  greet() {
      local __USED_SHELL="unknown"
      if [ -n "${ZSH_NAME}" ]; then __USED_SHELL="zsh"; fi
      if [ -n "${BASH}" ];     then __USED_SHELL="bash"; fi

      echo ""
      echo "Hello ${USER}."
      echo "I'm a ${__USED_SHELL} window at your service."
      echo ""
  }

  export DOTFILES="..."
  __finished
  ```

* Always use `${VAR}` over `$VAR` for sake of consistency (searching, vim, ...).

  _It helps a lot in doing automatic stuff like replacing code in an automatic way (e.g. using vi)._

  ```diff
  - $VAR
  - $1
  + ${VAR}
  + ${1}
  ```

* Use `constants` over `magic numbers` (or often used paths)!

  _Even the author will not know the meaning of every number after several months.
  And if he knows though, he will probably forget the precision of the constant and the places, where he has put them (-> bad for debugging)._

  ```zsh
  # BAD
  # because the path is often used

  if [ -d "<path to shell lib>/func" ]; then
      ...
  fi

  if [ -d "<path to shell lib>/prompts" ]; then
      ...
  fi



  # GOOD

  shell_lib="<path to shell lib>"
  if [ -d "${shell_lib}/func" ]; then
      ...
  fi

  if [ -d "${shell_lib}/prompts" ]; then
      ...
  fi
  ```

* Make __visibility as closest__ as possible.

  _Usually, programmer tend to not bother with visibility, but visibility helps a lot with getting nice and persistent interfaces._

  In shell, other scripts can be sourced, which acts like adding the code of the called script inside the calling script.
  Defined functions and fields are visible in the shells's environment.
  To remove them, call `unset <name>`.

* Use __white spaces around binary operators__.
  Per default, shell scripting is able to execute integer calculations, e.g. `echo $((3 + 4))`.
  Exceptions can be made for special cases to improve readability (see below).

  ```diff
  - e = (- a) * b;
  + e = (-a) * b;

  - e = a*b;
  + e = a * b;

  + e = a * b + c * d;    # ok, but not recommended here
  + e = a*b + c*d;        # improves readability
  ```

* Single quotes `'` preserve the literal value of each character, double quotes `"` interprete some of them.

  ```zsh
  $ echo "$(echo "hello")"
  hello

  $ echo '$(echo "hello")'
  $(echo "hello")
  ```

* `[[ ... ]]` vs `[ ... ]` vs `((...))` vs `(...)` vs `{...}`  
  See this super [stackoverflow answers][www_stackoverflow_brackets].
  In a nutshell:
  * `[[ ... ]]` is `bash-extension` and has additional features over `[ ... ]`, but latter is `POSIX` and preferred always.
  * `(...)` executes shell commands and influences execution order.
  * `((...))` executes arithmetic instructions (no floats)
  * `{...}` groups commands which only influences parsing, so it doesn't change the execution order. Example:  
    `x=2; { x=4; }; echo ${x}` prints `4` but  
    `x=2; ( x=4; ); echo ${x}` prints `2`

## Documentation <a name="documentation"></a>

* Separate module sections with `#-----#` (whole line).
  Take the following code snippet for inspiration.

  ```python
  #--------------------------------------------------------#
  # exports

  . "${shell_lib}/exports.sh"
  if [ -f "${custom_shell_lib}/exports.sh" ]; then
      . "${custom_shell_lib}/exports.sh"
  fi

  #--------------------------------------------------------#
  # aliases

  . "${shell_lib}/aliases.sh"
  if [ -f "${custom_shell_lib}/aliases.sh" ]; then
      . "${custom_shell_lib}/aliases.sh"
  fi
  ```

## Project Conventions <a name="project-conventions"></a>

* Prefer package/folder management over file mangement if `meaningful`.  
  __BUT:__ Think in an intuitive, handy and `deterministic`(!) way and don't take structuring and subfolding too far.

  Always ask yourself:  
  `How would most of the people search for this module/class/file?`  
  Someone without knowing the whole project structure should be able to find a file at the first try.  
  `In every folder, there should be only one option to continue searching (-> determinism).`


## Colors <a name="colors"></a>

```zsh
## in .bashrc
export LS_COLORS='rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:'

alias ls='ls --color=auto'
```


[www_wikipedia_zen_of_python]: https://en.wikipedia.org/wiki/Zen_of_Python
[www_wikipedia_python]: https://en.wikipedia.org/wiki/Python_(programming_language)#Features_and_philosophy
[www_stackoverflow_brackets]: https://stackoverflow.com/a/47576482
[www_github_koalaman_shellcheck]: https://github.com/koalaman/shellcheck

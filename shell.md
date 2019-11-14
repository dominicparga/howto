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

## File Style <a name="file-style"></a>

* Maximum line width is `80`.
  Exceptions can be made for String-constants and similar.

  _Humans have trouble reading the code with increasing line width.
  In general, more than `80` is not recommended._

* Use `4 spaces` for indention (p.s.: [could help salary](https://stackoverflow.blog/2017/06/15/developers-use-spaces-make-money-use-tabs)!).

## Coding Conventions <a name="coding-conventions"></a>

* Functions, fields and file names are written in `snake_case`.

  Since functions and fields are added to the shell's environment, their names are slightly changed to prevent conflicts or verbose autocompletion and help understanding the code:
  * private fields' names are in `snake_case`
  * exported ("public") fields' names are written in __CAPSLOCK__
  * private functions' names begin with __double underscore__
  * public functions' names doesn't begin with any underscore

  ```zsh
  # BAD
  Greet() {
      used_shell="unknown"
      # ...
  }

  export dotfiles="..."



  # GOOD
  # used in the shell, hence no leading dunderscore
  greet() {
      local used_shell="unknown"
      if [ -n "${ZSH_NAME}" ]; then used_shell="zsh"; fi
      if [ -n "${BASH}" ];     then used_shell="bash"; fi

      echo ""
      echo "Hello ${USER}."
      echo "I'm a ${used_shell} window at your service."
      echo ""
  }

  export DOTFILES="..."
  ```

* Always use `${VAR}` over `$VAR` for sake of consistency.

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

[www_wikipedia_zen_of_python]: https://en.wikipedia.org/wiki/Zen_of_Python
[www_wikipedia_python]: https://en.wikipedia.org/wiki/Python_(programming_language)#Features_and_philosophy
[www_stackoverflow_brackets]: https://stackoverflow.com/a/47576482

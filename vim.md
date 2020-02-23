# Vim

Vim is a way of navigating and editing text-files.
What makes vim special is its separation of __viewing__ text and __editing__ text.
For this, vim supports different modes with different key-usage.

- The __normal__-mode allows navigating through the text and executing handy commands, like "marking everything between brackets".
- The __insert__-mode allows adding new text.
- The __visual__ allows marking text, e.g. for deleting it.

There is a great tutorial for vim, which is probably already installed on your machine.
You can execute `vimtutor` in terminal and go.
Although the tutorial could be done in half an hour, it takes much longer to fully understand all commands and many commands are just not that important for most of the time.
This page provides a summary of the most important commands, which will cover more or less your whole daily vim-usage.

You can easily select vim in several IDEs, like [visual-studio-code][vscode] (and configure the hell out of it, which is not covered here).
With the overview of this page, it should be pretty easy to get into it. `:)`


## Table-of-contents

1. [Table-of-contents](#table-of-contents)
1. [Vim-inputs in general](#inputs-in-general)
1. [General commands](#general-commands)
1. [Basic cursor-movement](#basic-cursor-movement)
1. [Copy-and-paste](#copy-and-paste)
1. [Jumping words](#jumping-words)
1. [Jumping by search](#jumping-by-search)
1. [Jumping lines](#jumping-lines)
1. [Changing mode](#changing-mode)
1. [Targets](#targets)
1. [Deleting text without specified target](#deleting-text-without-target)
1. [Deleting text with target](#deleting-text-with-target)
1. [Replacing text](#replacing-text)
1. [Others](#others)


## Vim-inputs in general <a name="inputs-in-general"></a>

Inputs can be distinguished in 2 categories:

- targetless, like `move cursor one character right`
- targeted, like `delete next word`

When targeted input, the input contains the command (like `d` for __delete__), then a cursor-movement (`e` = __end__ of word) or a target (`iw` = __word__ where cursor is currently __in__).


Further, most commands can be repeated automatically by adding a number before the command.
While `w` jumps a word (see below), input `3w` will jump 3 words.


## General commands <a name="general-commands"></a>

|      input     |  mode  | action |
|:--------------:|:------:|:------:|
| <kbd>esc</kbd> | normal, visual, insert | Go to normal-mode. |
| <kbd>:w</kbd> | normal | Save file to disk. |
| <kbd>:q</kbd> | normal | Exit file/vim, but ask user before exiting, if file hasn't been saved. |
| <kbd>:q!</kbd> | normal | Force exit, independent whether the file has been saved or not. |
| <kbd>:x</kbd> | normal | short for `:wq` |
| <kbd>u</kbd> | normal | Undo changes. |
| <kbd>strg</kbd> + <kbd>r</kbd> | normal | Undo undo. |


## Basic cursor-movement <a name="basic-cursor-movement"></a>

|    input     | example |  mode  | action |
|:------------:|:--------|:------:|:------:|
| <kbd>h</kbd> | `li_ne 1` -> `l_ine 1` | normal | Move cursor left. |
| <kbd>l</kbd> | `li_ne 1` -> `lin_e 1` | normal | Move cursor right. |
| <kbd>j</kbd> | `li_ne 1` -> `li_ne 2` | normal | Move cursor down. |
| <kbd>k</kbd> | `li_ne 1` -> `li_ne 0` | normal | Move cursor up. |
| <kbd>0</kbd> | `Some text _in a line.` -> `_Some text in a line.` | normal | Move cursor to the start of line. |
| <kbd>$</kbd> | `Some text _in a line.` -> `Some text in a line._` | normal | Move cursor to the end of line. |
| <kbd>strg</kbd> + <kbd>u</kbd> || normal | Let cursor jump several lines up. |
| <kbd>strg</kbd> + <kbd>d</kbd> || normal | Let cursor jump several lines down. |

The current view can be changed.

|    input     |  mode  | action |
|:------------:|:------:|:------:|
| <kbd>strg</kbd> + <kbd>e</kbd> | normal | Let view move one line up. |
| <kbd>strg</kbd> + <kbd>y</kbd> | normal | Let view move one line down. |


## Copy-and-paste <a name="copy-and-paste"></a>

|      input     |  mode  | action |
|:--------------:|:------:|:------:|
| <kbd>y</kbd> | visual | Copy marked text. |
| <kbd>yy</kbd> | normal | Copy the cursor's current line. |
| <kbd>p</kbd> | normal, visual | Paste copied text at cursor. If some text is marked, it will be removed! If some text is marked, it will be removed! |
| <kbd>P</kbd> | normal, visual | Paste copied text after cursor's current character. If some text is marked, it will be removed! |

Note: Keep in mind that deleting text does store the deleted text in th clipbard.


## Jumping words <a name="jumping-words"></a>

|    input     | action | example |
|:------------:|:-------|:--------|
| <kbd>w</kbd> | Jump to the next first character of a word. | `he_llo, vim` -> `hello, _vim` |
| <kbd>W</kbd> | Jump to the next first character after a space. | `he_llo, vim` -> `hello, _vim` |
| <kbd>e</kbd> | Jump to the next last character of a word. | `he_llo, vim` -> `hell_o, vim` |
| <kbd>E</kbd> | Jump to the next last character before a space. | `he_llo, vim` -> `hello_, vim` |
| <kbd>b</kbd> | Jump to the previous first character of a word. | `hello, _vim` -> `hello_, vim` |
| <kbd>B</kbd> | Jump to the previous first character before a space. | `hello, _vim` -> `_hello, vim` |


## Jumping by search <a name="jumping-by-search"></a>

|    input     | action | example |
|:------------:|:-------|:--------|
| <kbd>f</kbd> + <kbd>any character (e.g. `i`)</kbd> | Jump to the next occurence of the provided character (inclusive). | `he_llo, vim` -> `hello, v_im` |
| <kbd>t</kbd> + <kbd>any character (e.g. `i`)</kbd> | Jump to the next occurence of the provided character (exclusive). | `he_llo, vim` -> `hello, _vim` |
| <kbd>F</kbd> + <kbd>any character (e.g. `l`)</kbd> | Jump to the previous occurence of the provided character (inclusive). | `hello, v_im` -> `hel_lo, vim` |
| <kbd>T</kbd> + <kbd>any character (e.g. `l`)</kbd> | Jump to the previous occurence of the provided character (exclusive). | `hello, v_im` -> `hell_o, vim` |


## Jumping lines <a name="jumping-lines"></a>

|    input     | action | example |
|:------------:|:-------|:--------|
| <kbd>42gg</kbd> | Jump to start of line 42. | `lin_e 5102` -> `_line 42` |
| <kbd>gg</kbd> | Jump to start of line 0. | `lin_e 5102` -> `_line 0` |
| <kbd>G</kbd> | Jump to start of last line. | `lin_e 5102` -> `_last line` |


## Changing mode <a name="changing-mode"></a>

|    input     | example |  mode  | action |
|:------------:|:--------|:------:|:------|
| <kbd>i</kbd> | `hell_o, vim` -> `hell_o, vim` | normal -> insert | Go to insert-mode in front of current character. |
| <kbd>I</kbd> | `hell_o, vim` -> `_hello, vim` | normal -> insert | Go to insert-mode in front of current line. |
| <kbd>a</kbd> | `hell_o, vim` -> `hello_, vim` | normal -> insert | Go to insert-mode behind current character. |
| <kbd>A</kbd> | `hell_o, vim` -> `hello, vim_` | normal -> insert | short for `$a` |
| <kbd>s</kbd> | `hell_o, vim` -> `hell_, vim` | normal -> insert | Remove cursor-character and go to insert-mode at this character's position. |
| <kbd>S</kbd> | `hell_o, vim` -> `_` | normal -> insert | Remove line's content (without the line-break) and go to insert-mode. |
| <kbd>o</kbd> | `hell_o, vim` -> `hell_o, vim \n |` | normal -> insert | Add a new line __below__ the cursor's current line, go to this line and enter insert-mode. |
| <kbd>O</kbd> | `hell_o, vim` -> `hello, vim \n _` | normal -> insert | Add a new line __above__ the cursor's current line, go to this line and enter insert-mode. |
| <kbd>v</kbd> | `hell_o, vim` -> `hell_o, vim` | normal -> visual | Go to visual-mode. After entering the visual-mode, you can move the cursor around and delete or copy this marked text to get back to normal-mode. |


## Targets <a name="targets"></a>

For examples, see their usage when [deleting text](#deleting-text) or [marking text](#marking-text).

|     input     | meaning |
|:-------------:|:--------|
| <kbd>i</kbd> + <kbd>some character</kbd> | Inner text between characters like brackets or quotations. |
| <kbd>a</kbd> + <kbd>some character</kbd> | Inner text between characters like brackets or quotations in addition to the specified characters. |


## Deleting text without specified target <a name="deleting-text-without-target"></a>

|    input      | example |  mode  | action |
|:-------------:|:--------|:------:|:------|
| <kbd>dd</kbd> | `line0 \n li_ne1 \n line2` -> `line0 \n _line2` | normal | Cut out the cursor's current line. |
| <kbd>ddp</kbd> | `line0 \n li_ne1 \n line2` -> `line0 \n line2 \n _line1` | normal | Handy command-order for swapping lines. |
| <kbd>D</kbd> | `line0 \n li_ne1 \n line2` -> `line0 \n li_ \n line2` | normal | Cut out the cursor's current line, starting from the cursor. |
| <kbd>C</kbd> | `line0 \n li_ne1 \n line2` -> `line0 \n li_ \n line2` | normal | short for `Da` |
| <kbd>x</kbd> | `line0 \n li_ne1 \n line2` -> `line0 \n li_e1 \n line2` | normal | Cut out the cursor's current character. |


## Deleting text with target <a name="deleting-text-with-target"></a>

Usually, deletions are initiated with `d`, followed by a cursor-movement-command (see above) or a target (see above).
You can delete text with `c` entering insert-mode afterwards.
In the following, some examples are given, working for both `d` and `c`.

|    input      | example |  mode  | action |
|:-------------:|:--------|:------:|:------|
| <kbd>de</kbd> | `he_llo, vim` -> `he_, vim` | normal | Delete to the next last character of a word (inclusive). |
| <kbd>dt</kbd> + <kbd>any character</kbd> | `he_llo, vim` -> `he_, vim` | normal | Delete to the next occurence of the provided character (exclusive). |
| <kbd>df</kbd> + <kbd>any character</kbd> | `he_llo, vim` -> `he_ vim` | normal | Delete to the next occurence of the provided character (inclusive). |
| ... | ... | ... | ... |
| <kbd>diw</kbd> | `he_llo, vim` -> `_, vim` | normal | Delete the current word to the next first character of a word. |
| <kbd>diW</kbd> | `he_llo, vim` -> `_ vim` | normal | Delete the current word to the next first character after a space (but keep the spaces). |
| ... | ... | ... | ... |
| <kbd>di</kbd> + <kbd>some character</kbd> | `hello, "v_im"` -> `hello, "_"` | normal | Delete all characters inside the provided character. Is the character a bracket, delete all characters inside these brackets. |
| <kbd>da</kbd> + <kbd>some character</kbd> | `hello, "v_im"` -> `hello, _` | normal | Delete all characters inside the provided character and the surrounding characters in addition. Is the character a bracket, delete all characters inside these brackets __and__ the brackets. |
| ... | ... | ... | ... |


## Replacing text <a name="replacing-text"></a>

|    input      | example |  mode  | action |
|:-------------:|:--------|:------:|:------|
| <kbd>r</kbd> + <kbd>any character</kbd> | `he_llo, vim` -> `he_klo, vim` | normal, visual | Replace cursor's character by the provided character. If multiple characters are marked, replaces every marked character by the provided one. |
| <kbd>R</kbd> + <kbd>any character</kbd> | `he_llo, vim` -> `hekkkkk_vim` | normal | Enter kind of a replace-mode, overwriting current text. |


## Others <a name="others"></a>

|    input      | example |  mode  | action |
|:-------------:|:--------|:------:|:------|
| <kbd>.</kbd> | `he_llo, vim` -> `he_lo, vim` -> `he_o, vim` | normal | Repeats the last executed command. |
| <kbd>strg</kbd> + <kbd>a</kbd> | `1` -> `2` | normal | Increments a number under the cursor. |
| <kbd>strg</kbd> + <kbd>x</kbd> | `2` -> `1` | normal | Decrements a number under the cursor. |


[vscode]: https://code.visualstudio.com/

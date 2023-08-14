# Vim and Cheatsheet

Vim is a way of navigating and editing text-files.
What makes vim special is its separation of __viewing__ text and __editing__ text.
For this, vim supports different modes with different key-usage.

- The __normal__-mode allows navigating through the text and executing other handy commands like searching or copy-paste.
- The __insert__-mode allows adding new text.
- The __visual__ allows marking text, e.g. for deleting it.

There is a great tutorial for vim, which is probably already installed on your machine.
You can execute `vimtutor` in terminal and go.
Although the tutorial could be done in half an hour, it takes much longer to fully understand all commands and many commands are just not that important for most of the time.
This page tries to solve this problem by providing a summary of the most important commands, which will cover more or less your whole daily vim-usage.

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
1. [More motions](#more_motions)
1. [Deleting text without specified motion](#deleting-text-without-motion)
1. [Deleting text with motion](#deleting-text-with-motion)
1. [Replacing text](#replacing-text)
1. [Others](#others)


## Vim-inputs in general <a name="inputs-in-general"></a>

Inputs can be distinguished in 2 categories:

- without motion, like `move cursor one character right`
- with motion, like `delete until next word`

When using a motion, the input consists of the command (like `d` for __delete__) followed by a cursor-movement (like `e` = __end__ of word) or a composite cursor-movement (`iw` = __word__ where cursor is currently __in__).
That is basically all to know.
The rest of vim is using and learning commands and motions.

Further, most commands can be repeated automatically by adding a number before the command.
While `w` jumps a word (see below), input `3w` will jump 3 words.

Via `:`, you might execute vim-commands, which is not explained further here.
This page just covers basics like saving the file.

> In the following, a cursor is marked as `hel[l]o`.


## General commands <a name="general-commands"></a>

|      input     |  mode  | action |
|:--------------:|:------:|:-------|
| <kbd>esc</kbd> | normal, visual, insert | Go to normal-mode. |
| <kbd>:w</kbd> | normal | Save file to disk. |
| <kbd>:q</kbd> | normal | Exit file/vim, but ask user before exiting, if file hasn't been saved. |
| <kbd>:q!</kbd> | normal | Force exit, independent whether the file has been saved or not. |
| <kbd>:x</kbd> | normal | short for `:wq`, so saving followed by exiting |
| <kbd>u</kbd> | normal | Undo changes. |
| <kbd>strg</kbd> + <kbd>r</kbd> | normal | Redo = Undo undo = Undo inverse. |
| <kbd>/</kbd> (or <kbd>?</kbd>) | normal | Enter search-pattern afterwards, searching forward (or backwards) |
| <kbd>#</kbd> | normal | Search backwards, but with current word as search-pattern |
| <kbd>n</kbd> (or <kbd>N</kbd>) | normal | Jump to next (previous) occurence of last search-pattern. |


## Basic cursor-movement <a name="basic-cursor-movement"></a>

All the following are considered to be motions.

|    input     | example |  mode  | action |
|:------------:|:--------|:------:|:-------|
| <kbd>h</kbd> | `li[n]e 1` -> `l[i]ne 1` | normal | Move cursor left. |
| <kbd>l</kbd> | `li[n]e 1` -> `lin[e] 1` | normal | Move cursor right. |
| <kbd>j</kbd> | `li[n]e 1` -> `li[n]e 2` | normal | Move cursor down. |
| <kbd>k</kbd> | `li[n]e 1` -> `li[n]e 0` | normal | Move cursor up. |
| <kbd>0</kbd> | `__Some tex[t].` -> `[_]_Some text.` | normal | Move cursor to the start of line. |
| <kbd>^</kbd> | `__Some tex[t].` -> `__[S]ome text.` | normal | Move cursor to the start of line, excluding whitespaces. This is similar to regular expressions (<kbd>^</kbd>, <kbd>$</kbd>). |
| <kbd>$</kbd> | `Some text [i]n a line.` -> `Some text in a line[.]` | normal | Move cursor to the end of line. This is similar to regular expressions (<kbd>^</kbd>, <kbd>$</kbd>). |

These are not motions, but handy.

|    input     | example |  mode  | action |
|:------------:|:--------|:------:|:-------|
| <kbd>strg</kbd> + <kbd>u</kbd> || normal | Let cursor jump several lines up. |
| <kbd>strg</kbd> + <kbd>d</kbd> || normal | Let cursor jump several lines down. |

The current view can be moved, instead of the cursor.

|    input     |  mode  | action |
|:------------:|:------:|:-------|
| <kbd>zz</kbd> | normal | Move view such that your cursor is centered. |
| <kbd>strg</kbd> + <kbd>e</kbd> | normal | Let view move one line up. |
| <kbd>strg</kbd> + <kbd>y</kbd> | normal | Let view move one line down. |


## Copy-and-paste <a name="copy-and-paste"></a>

You can change to visual-mode as described [below](#changing-mode).

|      input     |  mode  | action |
|:--------------:|:------:|:-------|
| <kbd>y</kbd> | visual | Copy marked text. |
| <kbd>yy</kbd> | normal | Copy the cursor's current line. |
| <kbd>p</kbd> | normal, visual | Paste copied text at cursor. If some text is marked, it will be removed! If some text is marked, it will be removed! |
| <kbd>P</kbd> | normal, visual | Paste copied text in front of cursor's current character. If some text is marked, it will be removed! |

> Note: Keep in mind that deleting text does store the deleted text in the clipbard.


## Jumping words <a name="jumping-words"></a>

Again, all inputs are motions.

|    input     | mode | action | example |
|:------------:|:----:|:-------|:--------|
| <kbd>w</kbd> | normal, visual | Jump to the next first character of a word. | `he[l]lo, vim` -> `hello[,] vim` |
| <kbd>W</kbd> | normal, visual | Jump to the next first character after a space. | `he[l]lo, vim` -> `hello, [v]im` |
| <kbd>e</kbd> | normal, visual | Jump to the next last character of a word. | `he[l]lo, vim` -> `hell[o], vim` |
| <kbd>E</kbd> | normal, visual | Jump to the next last character before a space. | `he[l]lo, vim` -> `hello[,] vim` |
| <kbd>b</kbd> | normal, visual | Jump to the previous first character of a word. | `hello, [v]im` -> `hello[,] vim` |
| <kbd>B</kbd> | normal, visual | Jump to the previous first character before a space. | `hello, [v]im` -> `[h]ello, vim` |


## Jumping by search <a name="jumping-by-search"></a>

And more motions..

|    input     | mode | action | example |
|:------------:|:----:|:-------|:--------|
| <kbd>f</kbd> + <kbd>any character (e.g. `i`)</kbd> | normal, visual | Jump to the next occurence of the provided character (inclusive). | `he[l]lo, vim` -> `hello, v[i]m` |
| <kbd>t</kbd> + <kbd>any character (e.g. `i`)</kbd> | normal, visual | Jump to the next occurence of the provided character (exclusive). | `he[l]lo, vim` -> `hello, [v]im` |
| <kbd>F</kbd> + <kbd>any character (e.g. `l`)</kbd> | normal, visual | Jump to the previous occurence of the provided character (inclusive). | `hello, v[i]m` -> `hel[l]o, vim` |
| <kbd>T</kbd> + <kbd>any character (e.g. `l`)</kbd> | normal, visual | Jump to the previous occurence of the provided character (exclusive). | `hello, v[i]m` -> `hell[o], vim` |


## Jumping lines <a name="jumping-lines"></a>

Also motions..

|    input     | mode | action | example |
|:------------:|:----:|:-------|:--------|
| <kbd>42gg</kbd> | normal, visual | Jump to start of line 42. | `lin[e] 5102` -> `[l]ine 42` |
| <kbd>gg</kbd> | normal, visual | Jump to start of line 0. | `lin[e] 5102` -> `[l]ine 0` |
| <kbd>G</kbd> | normal, visual | Jump to start of last line. | `lin[e] 5102` -> `[l]ast line` |


## Changing mode <a name="changing-mode"></a>

|    input     | example |  mode before command | mode after command | action |
|:------------:|:--------|:--------------------:|:------------------:|:-------------------|
| <kbd>i</kbd> | `hell[o], vim` -> `hell\|o, vim` | normal | insert | Go to insert-mode in front of current character. |
| <kbd>a</kbd> | `hell[o], vim` -> `hello\|, vim` | normal | insert | Go to insert-mode behind current character. |
| <kbd>I</kbd> | `hell[o], vim` -> `\|hello, vim` | normal | insert | short for <kbd>0i</kbd> |
| <kbd>A</kbd> | `hell[o], vim` -> `hello, vim\|` | normal | insert | short for <kbd>$a</kbd> |
| <kbd>s</kbd> | `hell[o], vim` -> `hell\|, vim` | normal | insert | Remove character at cursor's position and go to insert-mode. |
| <kbd>S</kbd> | `hell[o], vim` -> `\|` | normal | insert | Remove line's content (without the line-break) and go to insert-mode. |
| <kbd>c</kbd> + motion | | normal | insert | Remove characters as defined by the motion and go to insert mode. |
| <kbd>C</kbd> + motion | | normal | insert | Remove characters until end of line and go to insert mode. Short for <kbd>d$a</kbd> or <kbd>Da</kbd> |
| <kbd>o</kbd> | `hell[o], vim` -> `hello, vim \n \|` | normal | insert | Add a new line __below__ the cursor's current line, go to this line and enter insert-mode. |
| <kbd>O</kbd> | `hell[o], vim` -> `\| \n hello, vim` | normal | insert | Add a new line __above__ the cursor's current line, go to this line and enter insert-mode. |
| <kbd>v</kbd> | `hell[o], vim` -> `hell[o], vim` | normal | visual | Go to visual-mode. After entering the visual-mode, you can move the cursor around and delete or copy this marked text to get back to normal-mode. |
| <kbd>V</kbd> | `hell[o], vim` -> `hell[o], vim` | normal | visual | Go to visual-mode, marking lines instead of characters. After entering the visual-mode, you can move the cursor around and delete or copy this marked text to get back to normal-mode. |
| <kbd>strg</kbd> + <kbd>v</kbd> | | normal | visual | Enter block-selection. |


## More motions <a name="more_motions"></a>

These motions are entered after a command (like `d` for deleting).
For examples, see their usage when [deleting text](#deleting-text) or [marking text](#marking-text).

|     input     | meaning |
|:-------------:|:--------|
| <kbd>i</kbd> + <kbd>some character</kbd> | Text (i)nside enclosing characters like brackets or quotations. Example: mark all text inside brackets without the brackets. |
| <kbd>a</kbd> + <kbd>some character</kbd> | Text around enclosing characters like brackets or quotations, plus the specified characters itself. Example: mark all text inside brackets and the brackets. |

> Note: 'Some character' means enclosing characters, like brackets, quotations or `<`, `>`.


## Deleting text without specified motion <a name="deleting-text-without-motion"></a>

|    input      | example |  mode  | action |
|:-------------:|:--------|:------:|:-------|
| <kbd>dd</kbd> | `line0 \n li[n]e1 \n line2` -> `line0 \n [l]ine2` | normal | Cut out the cursor's current line. |
| <kbd>ddp</kbd> | `line0 \n li[n]e1 \n line2` -> `line0 \n line2 \n [l]ine1` | normal | Handy command-order for swapping lines. |
| <kbd>D</kbd> | `line0 \n li[n]e1 \n line2` -> `line0 \n li[] \n line2` | normal | Cut out the cursor's current line, starting from the cursor. |
| <kbd>C</kbd> | `line0 \n li[n]e1 \n line2` -> `line0 \n li[] \n line2` | normal -> insert | short for <kbd>Da</kbd>. A small <kbd>c</kbd> needs a motion like <kbd>d</kbd> (see [below](#deleting-text-with-motion)). |
| <kbd>x</kbd> | `line0 \n li[n]e1 \n line2` -> `line0 \n li[e]1 \n line2` | normal, visual | Cut out the cursor's current character (or the marked text in visual-mode). |


## Deleting text with motion <a name="deleting-text-with-motion"></a>

Usually, deletions are initiated with `d`, followed by a cursor-movement-command (see above) or a motion (see above).
You can delete text with `c` entering insert-mode afterwards.
In the following, some examples are given, working for both `d` and `c`.

|    input      | example |  mode  | action |
|:-------------:|:--------|:------:|:-------|
| <kbd>de</kbd> | `he[l]lo, vim` -> `he[,] vim` | normal | Delete to the next last character of a word (inclusive). |
| <kbd>dt</kbd> + <kbd>any character</kbd> | `he[l]lo, vim` -> `he[,] vim` | normal | Delete to the next occurence of the provided character (exclusive). |
| <kbd>df</kbd> + <kbd>any character</kbd> | `he[l]lo, vim` -> `he[ ]vim` | normal | Delete to the next occurence of the provided character (inclusive). |
| ... | ... | ... | ... |
| <kbd>diw</kbd> | `he[l]lo, vim` -> `[,] vim` | normal | Delete the current word to the next first character of a word. |
| <kbd>diW</kbd> | `he[l]lo, vim` -> `[ ]vim` | normal | Delete the current word to the next first character after a space (but keep the spaces). |
| ... | ... | ... | ... |
| <kbd>di</kbd> + <kbd>some character</kbd> | `hello, "v[i]m"` -> `hello, "["]` | normal | Delete all characters inside the provided character. Is the character a bracket, delete all characters inside these brackets. |
| <kbd>da</kbd> + <kbd>some character</kbd> | `hello, "v[i]m"` -> `hello,[ ]` | normal | Delete all characters inside the provided character and the surrounding characters in addition. Is the character a bracket, delete all characters inside these brackets __and__ the brackets. |
| ... | ... | ... | ... |


## Replacing text <a name="replacing-text"></a>

|    input      | example |  mode  | action |
|:-------------:|:--------|:------:|:-------|
| <kbd>r</kbd> + <kbd>any character</kbd> | `he[l]lo, vim` -> `he[k]lo, vim` | normal, visual | Replace cursor's character by the provided character. If multiple characters are marked, replaces every marked character by the provided one. |
| <kbd>R</kbd> + <kbd>any character</kbd> | `he[l]lo, vim` -> `hekkkkk[v]im` | normal | Enter kind of a replace-mode, overwriting current text. |


## Others <a name="others"></a>

|    input      | example |  mode  | action |
|:-------------:|:--------|:------:|:-------|
| <kbd>.</kbd> | `he[l]lo, vim` -> `he[l]o, vim` -> `he[o], vim` | normal | Repeats the last executed command. |
| <kbd>strg</kbd> + <kbd>a</kbd> | `1` -> `2` | normal | Increments a number under the cursor. |
| <kbd>strg</kbd> + <kbd>x</kbd> | `2` -> `1` | normal | Decrements a number under the cursor. |
| <kbd>%</kbd> | `((hello, vim[)])` -> `([(]hello, vim))` | normal, visual | Jump to opposite bracket. |


[vscode]: https://code.visualstudio.com/

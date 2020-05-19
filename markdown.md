# Markdown

If you stuck with syntax (e.g. how to include images?), checkout this [cheatsheet][github/adam-p/markdown-here/wiki/cheatsheet].
Below comes a table of contents.


## Table of Contents <a name="toc"></a>

1. [Table of Contents][self/toc]
1. [Links][self/links]
1. [Images][self/imgs]
1. [Emoji][self/emoji]
1. [Style mentions][self/style-mentions]
1. [Code-blocks][self/code-blocks]
1. [Super Fancy Stuff][self/super-fancy-stuff]

This TOC's source code is shown below.
Please notice that every item starts with number 1.
Also cool is the inline html tag, that allows title names being independent of the tag for the TOC.

Typically, the table of contents doesn't appear in the TOC, but here, this content is referred to the chapter.

```markdown
1. [Table of Contents][self/toc]
1. [Links][self/links]
1. [Images][self/imgs]
1. [Emoji][self/emoji]
1. [Style mentions][self/style-mentions]
1. [Code-blocks][self/code-blocks]
1. [Super Fancy Stuff][self/super-fancy-stuff]

...


## Super Fancy Stuff <a name="super-fancy-stuff"></a>

...
```


## Links <a name="links"></a>

Use links [directly](https://github.com/dominicparga) or with a [reference][github/dominicparga] in the end of the file.

I prefer using references instead of URLs and the following pros are my reasons to continue putting the links collected at the bottom of a file:

- I had to change some links, which is easier, if you have all links at one spot. That's extra handy when it comes to CHANGELOG.md when working with vim.
- With visual-studio-code and vim, it is easy to mark all the lines and sort them alphabetically, which groups same links and increases the overview.
- Some references and especially nested links (like in badges or images) are easier to understand for me, if I put all links to the bottom and use the shortened reference-name instead of the long and clunky URL.

```markdown
Use links [directly](https://github.com/dominicparga) or with a [reference][github/dominicparga] in the end of the file.

...

[github/dominicparga]: https://github.com/dominicparga
```


## Images <a name="imgs"></a>

To include images, you can use [markdown][github/adam-p/markdown-here/wiki/cheatsheet/images] or [html][stackoverflow/md-image-via-html].
Paths are relative to the README containing the line.

```markdown
![Replacement if image not found](path/to/image.png "Text when hovering over the image")
```

```html
<img src="path/to/image.png" title="Text when hovering over the image" alt="Replacement if image not found" width="256" height="256"/>
```

> Note: You can dump width or height and only provide one of them.
> The other one scales automatically.


## Emoji <a name="emoji"></a>

[Here][github/rxaviers/list-of-emojis] is a list of emoji and their codes (e.g. :smirk: `:smirk:`) in markdown.


## Style mentions <a name="style-mentions"></a>

Writing markdown is a lot easier, especially if you are vim-user, if every sentence has its own line without any linewidth limit.

```diff
+ This is a sentence.
+ This is a second sentence written in a separate line. :)

- This is a bad example. This is another sentence in the same line.
```

> __Note__: Here stands a note.
> `diff` is a quite useful code-style.
> As you see here, even notes can follow the multiline rule.
> Notes' lines start with `>`.

You can look at this files raw version to see the written style, but in addition:

- Never add two __headings__ right after each other, but add at least one sentence in between.
  Just looks more professional.
- Add __sub-headings__ only if *__more__* than one sub-heading is added.
  Otherwise, sub-headings make no sense.
- It helps using `__bold__` for __bold__ text and `*italic*` for *italic* text.
  Mixing them could be done like `*__bold and italic__*`, giving *__bold and italic__*, but you should be consistent.
- Horizontal lines (add `---` to an empty line) could help with readability.


## Code-blocks <a name="code-blocks"></a>

Every code block should define a style.
Some examples (given in a code block):

```text
- text
- python
- bash
- zsh
- java
- rust
- diff
- markdown
```

Highlighted monospace text can be written like `this`.


## Super Fancy Stuff <a name="super-fancy-stuff"></a>

<details>
<summary>Summary of a hidden text</summary>
Hidden text hihi.
</details>

```markdown
<details>
<summary>Summary of a hidden text</summary>
Hidden text.
</details>
```

badges ([`shields.io`][shields]) like

[![License][github/self/license/badge]][github/self/license]

[Visual Studio Code Linter Plugin][vscode/marketplace/markdownlint] enabling in-place linting of `markdown` files and thus ensuring consistency of Markdown files.

[awesome markdown list][github/mundimark/awesome-markdown] - an [awesome list][github/topics/awesome-list] showing the most awesome things one can do with markdown.


[github/adam-p/markdown-here/wiki/cheatsheet]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
[github/adam-p/markdown-here/wiki/cheatsheet/images]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#images
[github/dominicparga]: https://github.com/dominicparga
[github/mundimark/awesome-markdown]: https://github.com/mundimark/awesome-markdown/pull/26/files
[github/rxaviers/list-of-emojis]: https://gist.github.com/rxaviers/7360908
[github/self/license]: https://github.com/dominicparga/howto/blob/nightly/LICENSE
[github/self/license/badge]: https://img.shields.io/github/license/dominicparga/howto
[github/topics/awesome-list]: https://github.com/topics/awesome-list
[self/code-blocks]: #code-blocks
[self/emoji]: #emoji
[self/imgs]: #imgs
[self/links]: #links
[self/style-mentions]: #style-mentions
[self/super-fancy-stuff]: #super-fancy-stuff
[self/toc]: #toc
[shields]: https://shields.io
[stackoverflow/md-image-via-html]: https://stackoverflow.com/a/14747656
[vscode/marketplace/markdownlint]: https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint

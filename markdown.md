# Markdown

Below comes a table of contents.

## Table of Contents

1. [Super Duper Hardcore Mega Fancy Title](#fancy-title)
    1. [Code styles](#code-styles)
    2. [Style mentions](#style-mentions)

Cool is the inline html tag, that allows title names independent of the tag for the TOC.

## Super Duper Mega Fancy Title <a name="fancy-title"></a>

Writing markdown is a lot easier, especially if you are vim-user, if every sentence has its own line without any linewidth limit.

```diff
+ This is a sentence.
+ This is a second sentence written in a separate line. :)

- This is a bad example. This is another sentence in the same line.
```

> __Note__: Here stands a note.
> `diff` is a quite useful code-style.
> As you see here, even notes can follow the multiline rule.

### Code-styles <a name="code-styles"></a>

Every code block should define a style.
Some examples:

- text
- python
- bash
- zsh
- java
- rust
- diff

### Style mentions <a name="style-mentions"></a>

You can look at this files raw version to see the written style, but in addition:

- Never add two __headings__ right after each other, but add at least one sentence in between.
  Just looks more professional.
- Add __sub-headings__ only if *__more__* than one sub-heading is added.
  Otherwise, sub-headings make no sense.
- It helps using `__bold__` for __bold__ text and `*italic*` for *italic* text.
  Mixing them could be done like `*__bold and italic__*`, giving *__bold and italic__*, but you should be consistent.

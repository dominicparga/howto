# git

This page describes how to work with git in a pretty way.

## [Git Commit Messages][website_git_commit_messages]

Commit messages are a _hugely_ important part of working with git.
They not only help other workers to understand changes quickly, but also are the basement for new releases and their release notes.
Thus, these following rules [cited from here][website_git_commit_messages] should be accounted in commits.

First of all, commits should be `atomic`.
One commit should contain only changes of a few lines of code (or one single feature).
This method seems to be too verbose and kind of annoying, but when working with Git logs (`git log`) or GitHub's network tree, this is a huge advantage.
Branch management, releases and especially finding bugs is way easier with small commit messages.

In summary, a properly formed Git commit subject line should always be able to complete the following sentence:  
  `This commit <subject line>`

Some points about the commit message style:

* Separate `subject` from `body` with a blank line.
  The body explains _what_ has changed and _why_, not _how_ it has changed.
  _How_ can be checked by looking at the commit changes itself.
* Line widths
  * 1st line (`subject`) up to 50 characters
  * 2nd line empty
  * Remaining (`body`) lines up to 72 characters
* Lowercase the `subject` line

  ```diff
  - Fixes typo ...
  + fixes typo ...
  ```

* Do not end the `subject` line with a period

  ```diff
  - refactor brackets of some if-statements.
  + refactor brackets of some if-statements
  ```

* Use the present tense  

  ```diff
  - added feature
  + adds feature
  ```

* Use the 3rd person singular mood, no other language styles (no description either)  

  ```diff
  - move cursor to ...
  - fixed bug ...
  - sweet new API methods ...
  + moves cursor to ...
  + fixes bug ...
  + adds new API methods for ...
  ```

Consider using following verbs/flags in commit messages:

* `fix` when the commit contains bug fixes
* `doc(s)` when writing documentation
* `test(s)` when tests were changed/added
* `style` when code or format style changes occur in the commit
* `refactor` when changes __DO NOT__ change functionality

## [Gitflow Workflow][website_gitflow_workflow]

This project uses [Gitflow Workflow][website_gitflow_workflow], a nice and clear way to work effectively.

This means following branches are used:

* `master`: the official release (using tags)
* `develop`: branch for active development
* `release/<tag>`: temporary branch off `develop` for bug fixes and docs before getting merged into `master`
* `feature/<name>`: branches for specific feature development
* `hotfix/<name>`: branches for bug fixes branched off `master`
* `fix/<name>`: branches for bug fixes branched off `develop`

Following the rules of this, the `master` only contains releases and is only merged `--no-ff`.
This helps publishing clean releases, but is a bit redundant due to the nice feature-branch concept.
It helps a lot to keep in mind that `master` should always run without errors and that commits from `develop` could be squashed before merged into `master`.
If the `master` itself is the "release", it is probably more convenient to merge fast-forwarded if possible.

[website_git_commit_messages]: https://chris.beams.io/posts/git-commit
[website_gitflow_workflow]: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

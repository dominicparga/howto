# git

This page describes how to work with git in a pretty way.

## [Git Commit Messages][www_git_commit_messages]

Commit messages are a _hugely_ important part of working with git.
They not only help other workers to understand changes quickly, but also are the basement for new releases and their release notes.
Thus, these following rules [cited from here][www_git_commit_messages] should be accounted in commits.

First of all, commits should be `atomic`.
One commit should contain only changes of a few lines of code (or one single feature).
This method seems to be too verbose and kind of annoying, but when working with Git logs (`git log`) or GitHub's network tree, this is a huge advantage.
Branch management, releases and especially finding bugs is way easier with small commit messages.

In summary, a properly formed Git commit subject line should always be well structured, start with a verb and informative.
Besides that, it depends on your personal taste.
A commit message could base on completing the following sentence:  
  `This commit will <subject line>`  
Alternatively, you could use third person:  
  `This commit <subject line>`

In the following suggestions, the first version is used.

* Separate `subject` from `body` with a blank line.
  The body explains _what_ has changed and _why_, not _how_ it has changed.
  _How_ can be checked by looking at the commit changes itself.

* Line widths
  * 1st line (`subject`) up to 50 characters
  * 2nd line empty
  * Remaining (`body`) lines up to 72 characters

* Uppercase the `subject` line

  ```diff
  - fix typo ...
  + Fix typo ...
  ```

* Do not end the `subject` line with a period

  ```diff
  - Refactor brackets of some if-statements.
  + Refactor brackets of some if-statements
  ```

* Use the present tense  

  ```diff
  - Added feature ...
  - move cursor to ...
  - fixed bug ...
  - sweet new API methods ...
  + Add feature ...
  + Move cursor to ...
  + Fix bug ...
  + Add new API methods for ...
  ```

* Be informative!

  ```diff
  - Add build-feature
  + Add script to build xyz automatically
  ```

Consider using following verbs/flags in commit messages:

* `fix` when the commit contains bug fixes
* `doc(s)` when writing documentation
* `test(s)` when tests were changed/added
* `style` when code or format style changes occur in the commit
* `refactor` when changes __DO NOT__ change functionality

## [Gitflow Workflow][www_gitflow_workflow]

This project uses [Gitflow Workflow][www_gitflow_workflow], a nice and clear way to work effectively.

This means following branches are used:

* `master`: the official release (using tags)
* `develop`: branch for active development
* `release/<tag>`: temporary branch off `develop` for bug fixes and docs before getting merged into `master`
* `feature/<name>`: branches for specific feature development
* `hotfix/<name>`: branches for bug fixes branched off `master`
* `fix/<name>`: branches for bug fixes branched off `develop`

Following the rules of this, the `master` only contains releases and is only merged `--no-ff`.
Although it feels a bit redundant due to the nice feature-branch concept, this helps publishing clean releases and maintaining a clean git history.
Further, it helps keeping in mind that `master` should always run without errors.

[www_git_commit_messages]: https://chris.beams.io/posts/git-commit
[www_gitflow_workflow]: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

## Submodule

### Removing a submodule

Quelle:
[stackoverflow](https://stackoverflow.com/questions/1260748/how-do-i-remove-a-submodule)

To remove a submodule you need to:

1. Delete the relevant section from the .gitmodules file.
2. Stage the .gitmodules changes `git add .gitmodules`
3. Delete the relevant section from .git/config.
4. Run `git rm --cached 'path/to/submodule'` (no trailing slash).
5. Run `rm -rf .git/modules/path/to/submodule`
6. Commit `git commit -m "Removed submodule 'name'"`
7. Delete the now untracked submodule files
8. `rm -rf 'path/to/submodule'`

### More sources

* [git doc](https://git-scm.com/book/de/v1/Git-Tools-Submodule)
* [cheatsheet](https://www.systutorials.com/5520/git-submodule-cheat-sheet/)

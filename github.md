# github

Some tips and info for using github projects for more than just storing your code. ;)

## Table of Contents

1. [About projects](#projects)
    1. [Kanban board](#kanban-board)
1. [Issues](#issues)
    1. [Labels](#labels)
    1. [Opening issues](#opening-issues)
    1. [Closing issues](#closing-issues)
1. [Pull Requests](#pull-requests)
    1. [Assignee vs Reviewer](#assignee-vs-reviewer)

## About Projects <a name="projects"></a>

TODO ([check this page][www_about_project_boards] as well)

### Project-board <a name="kanban-board"></a>

The project-board is separated in 5 columns.

|      Column      | Info |
|------------------|------|
| Backlog          | This column is not automated, because it's just collecting unplanned issues. |
| Todo             | Issues, which are in the current scope, are manually moved to this column. Reopened issues or Pull-Requests are moved to this column automatically. It is very likely, that the Backlog contains more work than can be worked on. |
| In Progress      | This column is automated, but does nothing automatically. With this, GitHub takes issues in this column into account when calculating the progress-bar. |
| In Review (beta) | Issues, whose branches are in Pull-Request to master, are in this column. |
| Done             | Finished tasks lands here. |

## Issues <a name="issues"></a>

Every task, that can be done in several days, should be wrapped into an issue.
So working with issues, reading and writing them, happens very often.
That's why they should follow an atomic structure and common format, so you can find relevant information faster.

For examples, have a look at this project's templates.
You find them in `.github/ISSUE_TEMPLATE/`.
When creating a new issue, GitHub takes these templates and asks the issue-creator to use them.

### Labels <a name="labels"></a>

Maybe, this list changes with time.
In general, one single label should not cover different kind of information, like type (e.g. `bugfix`, `feature`), status (e.g. `in-progress`) and priority (e.g. `high`, `middle`, `low`).
To provide these different kind of information via labels, prefixes help (e.g. `bugfix` becomes `type: bugfix`).

In my opinion, information like priority or status are related to the repository's state and shouldn't be used as label.
I prefer creating `Projects` (the register next to the `Wiki`) resulting in following labels.

- `bugfix`: Of course, this label is relevant for bugs.
  Special about this is the absence of a `hotfix`-label.
  Here holds the same argument as above: `hotfix` does imply priority and status, since it should be in progress immediately, which is covered by the project.
- `documentation`: Clearly, explanations and information about the repo or the code should be added.
- `duplicate`: If an issue addresses the same topic as another issue, discussions and similar should be part of one issue-card.
  The other issue-card gets this label.
- `feature`: This label refers to some "practical" work, like coding or setting up something.
  Improvements of existing features are covered by this label as well.

### Opening issues <a name="opening-issues"></a>

TODO

### Closing issues <a name="closing-issues"></a>

TODO ([check this page][www_closing_issues_using_keywords] as well)

## Pull Requests <a name="pull-requests"></a>

TODO

### Assignee vs. Reviewer <a name="assignee-vs-reviewer"></a>

TODO

[www_closing_issues_using_keywords]: https://help.github.com/en/articles/closing-issues-using-keywords
[www_about_project_boards]: https://help.github.com/en/articles/about-project-boards

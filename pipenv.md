# pipenv

Good page for getting general overview of `pipenv` is [here][www_pipenv_guide].

## Setup

For project-local environment folders, add this to your `shellrc`:

```zsh
export PIPENV_VENV_IN_PROJECT='yes'
```

More flags can be found [here][www_env_setup].

## Start

Just start with  
`pipenv install MODULE`.  
Pipenv will init by its own.

## At a glance

Found [here][www_docs]:
> *If a `.env` file is present in your project, `$ pipenv shell` and `$ pipenv run` will automatically load it.*

Further, the `--dev` flag like in  
`pipenv install --dev pylint`  
can be used to install modules for development only.

## `Pipfile` and `Pipfile.lock`

TL;DR: `Pipfile` defines dependency requirements, while `Pipfile.lock` actually represents an instance of them to reproduce the environment in a deterministic way.

Both files should be added to a repo (so none of them should be added to `.gitignore`). Look [here][www_pipfilelock_gitignore] for further info.

[www_pipenv_guide]: https://realpython.com/pipenv-guide/#example-usage
[www_env_setup]: https://pipenv.readthedocs.io/en/latest/advanced/#configuration-with-environment-variables
[www_docs]: https://pipenv.readthedocs.io/en/latest/advanced/
[www_pipfilelock_gitignore]: https://github.com/pypa/pipenv/issues/598

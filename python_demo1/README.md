
# python_demo1

## List Python runtime versions with pyenv

`$ pyenv install --list`

## Install Python runtime with pyenv

`$ pyenv install 3.10.3`

## Select local Python runtime

`$ pyenv local 3.10.3`

## Create Virtual Environment in project root folder

`$ export PIPENV_VENV_IN_PROJECT=true`

`$ pipenv --python $(pyenv which python)`

## Activate Virtual Environment

`$ pipenv shell`

## Deactivate Virtual Environment

`$ exit`

## Remove Virtual Environment

`$ pipenv --rm`
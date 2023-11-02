#!/bin/bash

export PIPENV_VENV_IN_PROJECT=true

pipenv --python $(pyenv which python)
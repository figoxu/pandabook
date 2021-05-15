#!/usr/bin/env bash
set -e

BASEDIR=$(dirname "$0")
cd $BASEDIR
cd ../

echo c.NotebookApp.notebook_dir = \'`pwd`\'  > ~/.jupyter/jupyter_notebook_config.py


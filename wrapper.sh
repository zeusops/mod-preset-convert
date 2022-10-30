#!/bin/sh

DIR="$(cd -- "$(dirname "$0")" > /dev/null 2>&1 ; pwd -P)"
$DIR/venv/bin/python $DIR/main.py "$@"

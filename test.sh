#! /bin/bash

PYTHON_VERSION=${PYTHON_VERSION}

test=$(python${PYTHON_VERSION} test.py)
echo $(ls)

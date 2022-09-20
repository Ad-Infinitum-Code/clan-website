#!/bin/bash

DEACTIVATE=0

# Check if venv is active, activate it if not and set variable to deactivate when done
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "activating venv"
    source venv/bin/activate
    DEACTIVATE=1
fi

# Generate the requirements files
pip-compile requirements.in
pip-compile dev-requirements.in

# Deactivate the venv if we activated it from this script
if [ $DEACTIVATE == 1 ]; then
    echo "deactivating venv"
    deactivate
fi
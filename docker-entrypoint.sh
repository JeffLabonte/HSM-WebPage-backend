#!/usr/bin/env bash
export FLASK_APP=main.py

cd src/ && flask run --host=0.0.0.0

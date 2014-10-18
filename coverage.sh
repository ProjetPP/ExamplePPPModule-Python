#!/bin/bash
python3-coverage run --source=example_ppp_module run_tests.py
python3-coverage html
xdg-open htmlcov/index.html

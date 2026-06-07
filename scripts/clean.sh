#!/bin/bash
rm -rf venv .pytest_cache .pylintcache
find . -name "*.pyc" -delete
find . -name "__pycache__" -delete
#!/usr/bin/env bash
set -euo pipefail
python -m pip install pyinstaller
pyinstaller --onefile --name MetaContextOS meta_context_framework.py

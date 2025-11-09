#!/usr/bin/env bash

pyinstaller -n spellcheck --distpath dist/linux src/main.py --onefile --specpath build/specs

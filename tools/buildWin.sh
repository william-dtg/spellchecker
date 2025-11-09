#!/usr/bin/env bash

PYTHON_VERSION=3.12.9
PYTHON_EXE_NAME=python-${PYTHON_VERSION}.exe
PYTHON_EXE_PATH=${BUILD_DIR}/${PYTHON_EXE_NAME}

# Initialize Wine prefix without GUI
xvfb-run -a wine cmd /c echo OK

# Download Python for Windows if not already downloaded
if [[ ! -f "$PYTHON_EXE_PATH" ]]; then
  echo "Downloading Python ${PYTHON_VERSION} for Windows..."
  wget -O "$PYTHON_EXE_PATH" "https://www.python.org/ftp/python/${PYTHON_VERSION}/${PYTHON_EXE_NAME}"
else
  echo "Python installer already exists in build/"
fi

# Install Python
xvfb-run -a wine "${PYTHON_EXE_PATH}" \
  /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 TargetDir=C:\\Python312

# Install PyInstaller inside Wine Python
wine C:\\Python312\\python.exe -m pip install pyinstaller

mkdir -p ${BUILD_DIR}/specs
wine pyinstaller -n spellcheck --distpath dist/windows src/main.py --onefile --specpath build/specs

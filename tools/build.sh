#!/usr/bin/env bash

# Where to store build artifacts
export BUILD_DIR=build

# Create build dir if it doesn't exist
mkdir -p "$BUILD_DIR"

# Build for each platform
./tools/buildWin.sh
./tools/buildLinux.sh

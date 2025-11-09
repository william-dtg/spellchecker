# Introduction
This is a very simple terminal program for checking if the words you are typing are spelled correctly. If they are, nothing happens, if they are not, they turn red, press enter to close the program.

# Installation
Download the executable file found in the windows or linux directory in dist and run the program as you would any other executable. Or clone this repo and run src/main.py directly ensuring that you have the correct correct packages installed, these can be found in the nix flake, or if you are on linux and have nix installed, you can run the flake and run tools/build.sh to build it from your machine.

# Why?
Because someone I know said it would be useful to them, and I thought it was a good excuse to mess around with an idea for a build system.

# How?
The program is a very basic python script that uses GNU aspell for the spell checking bundled into an executable with pyinstaller and dependencies managed by a nix flake. The tools directory holds the scripts required to build the program on both windows and linux from a linux machine (the windows build uses wine). Note I have not tested these build scripts work aside from my own machine but hopefully I have used nix correctly and it works on your linux machine as well!
This build scheme is totally overkill for the size of the project but hopefully this serves as a good proof of concept for the future.

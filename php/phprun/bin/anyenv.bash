#!/bin/bash
#
git clone https://github.com/riywo/anyenv ~/.anyenv
source bin/lang.bash 
#
mkdir -p $(anyenv root)/plugins;
git clone https://github.com/znz/anyenv-update.git $(anyenv root)/plugins/anyenv-update;
source bin/lang.bash 
#
anyenv install phpenv
anyenv install ndenv
source bin/lang.bash 

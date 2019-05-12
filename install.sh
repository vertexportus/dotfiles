#!/bin/bash

CURRENT_SCRIPT=`realpath $0`
BASE_PATH=`dirname $CURRENT_SCRIPT`

source $BASE_PATH/scripts/fonts.rc

# install fonts
install_fonts
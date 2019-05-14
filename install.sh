#!/bin/bash

CURRENT_SCRIPT=`realpath $0`
BASE_PATH=`dirname $CURRENT_SCRIPT`
SCRIPTS=$BASE_PATH/scripts

source $SCRIPTS/fonts.rc
source $SCRIPTS/configs.rc

# install fonts
create_config_links
install_fonts
check_env_vars
#!/usr/bin/env bash

## configs
# bigscreen_fontsize=10
# normalscreen_fontsize=14

## monitor and machine related stuff
monitor_primary=$(polybar -m | grep primary | sed "s/\s(.*)//g" | sed "s/:\s.*//g")
monitor_secondary=$(polybar -m | grep -v primary | sed "s/:\s.*//g")
monitor_primary_res=$(polybar -m | grep primary | sed "s/\s(.*)//g" | sed "s/.*:\s//g" | sed "s/x.*//g")
# echo $monitor_primary $monitor_secondary

# machine_name=$(cat /proc/sys/kernel/hostname)

## fonts
# if [[ "$machine_name" == "seth" ]]; then
#     fontsize0=$bigscreen_fontsize;
# else
#     fontsize0=$bigscreen_fontsize;
# fi
# fontsize1=$(($fontsize0 + 4))
# normalscreen_fontsize
# POLYBAR_FONT0="FuraCode Nerd Font Mono:style=Retina,Regular:size=${fontsize0}:antialias=true;3"
# POLYBAR_FONT1="FuraCode Nerd Font Mono:style=Retina,Regular:size=${fontsize1}:antialias=true;3"
# POLYBAR_FIXED_FONT0="FuraCode Nerd Font Mono:style=Retina,Regular:size=${fontsize0}:antialias=true;3"
# POLYBAR_FIXED_FONT1="FuraCode Nerd Font Mono:style=Retina,Regular:size=${fontsize1}:antialias=true;3"

# echo $POLYBAR_FONT0
# echo $POLYBAR_FONT1

polybar complete &
MONITOR=${monitor_secondary} polybar second &

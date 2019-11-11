#!/usr/bin/env bash

# you can also define some variables
# Black        0;30     Dark Gray     1;30
# Red          0;31     Light Red     1;31
# Green        0;32     Light Green   1;32
# Brown/Orange 0;33     Yellow        1;33
# Blue         0;34     Light Blue    1;34
# Purple       0;35     Light Purple  1;35
# Cyan         0;36     Light Cyan    1;36
# Light Gray   0;37     White         1;37
WHITE=$'\033[1;37m'
ORANGE=$'\033[0;33m'
RED=$'\033[0;31m'
BOLDRED=$'\033[1;31m'
INVRED=$'\033[1;97;41m'
GREEN=$'\033[1;32m'
CYAN=$'\033[0;36m'
BLUE=$'\033[0;34m'
LIGHTCYAN=$'\033[1;36m'
PURPLE=$'\033[0;35m'
LIGHTPURPLE=$'\033[1;35m'
YELLOW=$'\033[1;33m'

NC=$'\033[0m' # No Color

ASK_QUESTION=" ${YELLOW}??${NC} "
BREAK_CHAR=$'\n'
BREAK="${BREAK_CHAR}   ${YELLOW}>${NC} "
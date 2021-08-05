@echo off
title Beats2Save - backup

rem only change these 4 variables =================   no backslashes!  ==============

set gamedir="G:/Steam/steamapps/common"
set savedir="C:/Users/KampfKeks/AppData/LocalLow/Hyperbolic Magnetism"
set backupdir="G:/Beat Saber backups"
set max_backups=8

rem =================================================================================

python Beats2Save.py -g %gamedir% -s %savedir% -b %backupdir% -c -n %max_backups%
pause
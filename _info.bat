@echo off
title Beats2Save - info

rem only change these 3 variables =================   no backslashes!  ==============

set gamedir="G:/Steam/steamapps/common"
set savedir="C:/Users/KampfKeks/AppData/LocalLow/Hyperbolic Magnetism"
set backupdir="G:/Beat Saber backups"

rem =================================================================================

python Beats2Save.py -g %gamedir% -s %savedir% -b %backupdir% -i
pause

rem show informations about Beat Saber (BS-Version, Size, Backup dir size)

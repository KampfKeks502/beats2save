# Beats2Save

A simple python script that allows you to create and restore Beat Saber (PCVR/Steam) backups more easily.\
Script tested using Python 3.8 (64-bit) - Win10

# Screenshots
**Create a backup** (_backup.bat):

![Alt text](/../master/screenshots/backup.png?raw=true "_backup.bat")

**Restore from backup** (_restore.bat):

![Alt text](/../master/screenshots/restore.png?raw=true "_restore.bat")

**Show Beat Saber informations** (_info.bat):

![Alt text](/../master/screenshots/info.png?raw=true "_info.bat")

# How does it work
When starting a backup, the script copies the "Saves" directory (usually located in "C:\Users\\%username%\\AppData\LocalLow\Hyperbolic Magnetism\Beat Saber") and the "Game" directory ("...\steamapps\common\Beat Saber") to the desired backup folder. Doing so, it also creates a corresponding folder inside the backup location containing the Beat Saber version and time of the backup. Optionally you can specify how many backups you want to keep. If specified the script will only keep a certain amount of backups at a time.

When restoring a backup, the script allows you to select the backup you want to restore from. After that it will move the current Beat Saber installation to a folder called "trash" (located inside the backup folder) just in case you want to recover it. Then the script will start to recover the selected game version.

# How to use
Adjust the "save", "game", and "backup" paths inside "_backup.bat", "_restore.bat" and "_info.bat" to your needs.\
**!!! Important !!!** only use "/". **NO** backslashes. Also **environment variables** like "%username%" **won't work** so you have to paste in the full path.
1. "Save" path - usually located in "C:\Users\\%username%\\AppData\LocalLow\Hyperbolic Magnetism\"
2. "Game" path - path to your Steam lib e.g. "G:/Steam/steamapps/common"
3. "Backup" path - specify where you want your backup location to be [you have to create the folder first before starting the backup]

Adjust the max amount of total backups. E.g. -n 8 (max amount of backups set to 8).\
If 0 then it will be infinite.

Execute the *.bat file(s).


# Args
```test
usage: Beats2Save.py [-h] [-r | -c | -i] -s  -g  -b  [-n] [-d]

Create or Restore BeatSaber backups.

optional arguments:
  -h, --help           show this help message and exit
  -r, --restore        Restore from backup
  -c, --create         Create backup
  -i, --info           Show BS Version and Game/Backup dir size
  -s , --save_dir      BeatSaber save directory [e.g C:/Users/Kampfkeks/AppData/LocalLow/Hyperbolic Magnetism"]
  -g , --game_dir      BeatSaber/Steam game directory [e.g "G:/Steam/steamapps/common"]
  -b , --backup_dir    Backup directory [e.g "G:/Backup/Beatsaber"]
  -n , --max_backups   Max number of backups to store [0 = infinite]
  -d, --debug          enable debug mode
```

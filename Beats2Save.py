import argparse
import logging, sys
import os.path
from os import path
import os
import shutil
from datetime import datetime



# args
parser = argparse.ArgumentParser(description="Create or Restore BeatSaber backups.")

group_input = parser.add_mutually_exclusive_group()
group_input.add_argument("-r", "--restore", action="store_true", required=False, help="Restore from backup")
group_input.add_argument("-c", "--create", action="store_true", required=False, help="Create backup")
group_input.add_argument("-v", "--version", action="store_true", required=False, help="Show current BeatSaber version")

parser.add_argument("-s", "--save_dir", type=str, metavar="", required=True, help="BeatSaber save directory [e.g " + "C:/Users/Kampfkeks/AppData/LocalLow/Hyperbolic Magnetism" + "\"]")
parser.add_argument("-g", "--game_dir", type=str, metavar="", required=True, help="BeatSaber/Steam game directory [e.g \"G:/Steam/steamapps/common\"]")
parser.add_argument("-b", "--backup_dir", type=str, metavar="", required=True, help="Backup directory [e.g \"G:/Backup/Beatsaber\"]")

parser.add_argument("-n", "--max_backups", type=int, metavar="", required=False, default=0, help="Max number of backups to store")

args = parser.parse_args()


logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)5s]   %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",  
                    handlers=[logging.FileHandler("debug.log"),
                    logging.StreamHandler()])



def create(save_dir, game_dir, backup_dir, max_backups, version):

    now = datetime.now()
    time_str = now.strftime("%Y-%m-%d__%H-%M-%S")
    src = save_dir + "/Beat Saber"
    dst = backup_dir + "/BeatSaber_" + version + "__" + time_str + "/save/Beat Saber"
    logging.info("Starting Save backup...")
    copy(src, dst)
    logging.info("Finished")

    src = game_dir + "/Beat Saber"
    dst = backup_dir + "/BeatSaber_" + version + "__" + time_str + "/game/Beat Saber"
    logging.info("Starting Game backup...")
    copy(src, dst)
    logging.info("Finished")

    end_time = datetime.now()
    logging.info("Backup finished in: " + str(end_time-now))

    if not max_backups == 0:
        clean_backups(backup_dir, max_backups)

def restore(save_dir, game_dir, backup_dir, version):
    # list all
    dirs_raw = os.listdir(backup_dir)
    dirs = []
    # filter dir list
    for d in dirs_raw:
        if d.find('BeatSaber_') != -1:
            dirs.append(d)
    
    i = 1
    logging.info("Please select your desired backup and hit ENTER [e.g. 1, 2, 3, ...]")
    for d in dirs:
        logging.info(str(i) + ".  " + d)
        i += 1
    valid = False
    while not valid:
        number = int(input("Restore Backup Nr. "))
        if isinstance(number, int) and number >0 and number <= len(dirs):
            valid = True
        else:
            print("Invalid number")
    backupdir = dirs[number-1]
    logging.info("Restoring " + backupdir)

    # move current BS version to trash
    now = datetime.now()
    time_str = now.strftime("%Y-%m-%d__%H-%M-%S")
    src = save_dir + "/Beat Saber"
    dst = backup_dir + "/trash/BeatSaber_" + version + "__" + time_str + "/save/Beat Saber"
    logging.info("Moving Save directory to trash...")
    move(src, dst)
    logging.info("Finished")

    src = game_dir + "/Beat Saber"
    dst = backup_dir + "/trash/BeatSaber_" + version + "__" + time_str + "/game/Beat Saber"
    logging.info("Moving Game directory to trash...")
    move(src, dst)
    logging.info("Finished")

    # restore from backup
    src = backup_dir + "/" + backupdir + "/save/Beat Saber"
    dst = save_dir + "/Beat Saber"
    logging.info("Restoring Save from backup ...")
    copy(src, dst)
    logging.info("Finished")

    src = backup_dir + "/" + backupdir + "/game/Beat Saber"
    dst = game_dir + "/Beat Saber"
    logging.info("Restoring Game from backup ...")
    copy(src, dst)
    logging.info("Finished")

    end_time = datetime.now()
    logging.info("Backup restored in: " + str(end_time-now))

def check_dir(paths):
    if not path.exists(paths):
        logging.info("Path not found [" + paths + "]")
        sys.exit()


def bs_version(game_dir):
    file_location = game_dir + "/Beat Saber/UserData/Beat Saber IPA.json"
    if not path.exists(file_location):
        logging.info("Can't get BeatSaber Version. Unable to read File [" + file_location + "]")
    else:
        f = open(file_location, "r")
        #parse file for version
        for line in f:
            if line.find('LastGameVersion') != -1:
                version = line.split("\"")[3]  # BS version
                logging.info("BeatSaber Version found [" + version + "]")
                return version
                

def copy(src, dst):
    try:
        shutil.copytree(src, dst)
    except Exception as err:
        logging.info("Error copying files")
        print(err)
        sys.exit()


def move(src, dst):
    try:
        shutil.move(src, dst)
    except Exception as err:
        logging.info("Error moving files")
        print(err)
        sys.exit()



def clean_backups(backup_dir, max_backups):
    dirs = os.listdir(backup_dir)
    count = backup_count(dirs)
    if count> max_backups:
        print()
        logging.info("Max backups exceeded. Deleting old backup(s)...")
    while count > max_backups:
        logging.info("Deleting " + dirs[0] + " ...")
        shutil.rmtree(backup_dir + "/" + dirs[0])
        logging.info("Done")
        dirs = os.listdir(backup_dir)
        count = backup_count(dirs)
        


def backup_count(dirs):
    i = 0
    for d in dirs:
        if d.find('BeatSaber_') != -1:
            i += 1
    return i


if __name__ == "__main__":
    if not args.restore and not args.create and not args.version:
        sys.exit()
    logging.info("Beats2Save 1.0 by KampfKeks502")
    check_dir(args.save_dir)
    check_dir(args.game_dir)
    check_dir(args.backup_dir)
    print()
    logging.info("Path check PASSED")
    version = bs_version(args.game_dir)
    if args.create:
        print()
        logging.info("Creating backup")
        create(args.save_dir, args.game_dir, args.backup_dir, args.max_backups, version)
    elif args.restore:
        print()
        logging.info("Restoring backup")
        restore(args.save_dir, args.game_dir, args.backup_dir, version)
    elif args.restore:
        sys.exit()
        

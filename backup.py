import os
import shutil
import datetime
import schedule
import time

source_dir = "/Users/shaharishay/Documents/test"
destination_dir = "/Users/shaharishay/Documents/backup"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    destination_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, destination_dir)
        print(f"Folder copied to: {destination_dir}")
    except FileExistsError:
        print(f"Folder already exsits in: {dest}")

copy_folder_to_directory(source_dir, destination_dir)       
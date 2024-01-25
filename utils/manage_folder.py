import os
from shutil import rmtree

def create_dir(folder_name):
    if os.path.isdir(f"{folder_name}"):
        rmtree(f"{folder_name}")

    os.makedirs(f"{folder_name}")
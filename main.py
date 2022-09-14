import os.path
from pathlib import Path
import readline  # Don't delete this, so you can use arrow key when input string

from execute import execute

# ------------------------SETTINGS-------------------------------
manually = False
resume_file_path = "/path/to/resume"
torrent_file_path = "/path/to/torrents"
debug = False  # Just output the command to be executed, nothing will happen to disk
# ---------------------------------------------------------------


if manually is False:
    tr_config_path = os.path.join(str(Path.home()), ".config/transmission")
    if not os.path.exists(tr_config_path):
        print("Transmission config path not found, please edit main.py to manually set the path")
        exit(1)
    else:
        print(f"Transmission config path found: {tr_config_path}")
        resume_file_path = os.path.join(tr_config_path, "resume")
        torrent_file_path = os.path.join(tr_config_path, "torrents")
        target_base = input("Press ENTER to extract to current folder, or input a new one: ")
        if target_base == "":
            target_base = os.path.join(os.path.dirname(os.path.realpath(__file__)), "extract")

        execute(resume_file_path, torrent_file_path, target_base, debug)

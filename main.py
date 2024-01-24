import os.path
from pathlib import Path
import readline  # Don't delete this, otherwise arrow key cannot be used when inputting

from execute import execute

# ------------------------SETTINGS-------------------------------
test_run = False  # Just output the command to be executed, nothing will happen to disk
# ---------------------------------------------------------------

tr_config_path = os.path.join(str(Path.home()), ".config/transmission")
resume_file_path = os.path.join(tr_config_path, "resume")
torrent_file_path = os.path.join(tr_config_path, "torrents")

while not os.path.exists(resume_file_path) or not os.path.exists(torrent_file_path):
    tr_config_path = input("Data not found, please specify transmission's config path:")
    resume_file_path = os.path.join(tr_config_path, "resume")
    torrent_file_path = os.path.join(tr_config_path, "torrents")

print(f"Using config path: {tr_config_path}")
target_base = input("Input path to save torrents, or press Enter to use current location:")
if target_base == "":
    target_base = os.path.join(os.path.dirname(os.path.realpath(__file__)), "torrent_extract")

execute(resume_file_path, torrent_file_path, target_base, test_run)

# bencode_open is an open-source MIT-licensed library, refer to: https://github.com/imachug/bencode-open

from lib import bencode_open
import os
import subprocess


def extract_resume_file(file):
    with open(file, "rb") as f:
        content = bencode_open.loads(f.read())
    name = content[b"name"].decode("utf-8")
    path = content[b"destination"].decode("utf-8")
    return name, path


def extract_torrent_file(file):
    with open(file, "rb") as f:
        content = bencode_open.loads(f.read())
    name = content[b"info"][b"name"].decode("utf-8")
    return name, file


def execute(resume_file_path, torrent_file_path, target_base, debug=False):
    resume_list = []
    torrent_list = []
    print("Loading resume/torrent files...")
    for (root, dirs, files) in os.walk(resume_file_path):
        for file in files:
            if file[-6:] == "resume":
                resume_info = extract_resume_file(os.path.join(resume_file_path, file))
                resume_list.append(resume_info)

    for (root, dirs, files) in os.walk(torrent_file_path):
        for file in files:
            if file[-7:] == "torrent":
                torrent_info = extract_torrent_file(os.path.join(torrent_file_path, file))
                torrent_list.append(torrent_info)
    print("Loaded, now matching...")

    match_count = 0
    no_match_count = 0
    match_flag = 0

    for torrent_info in torrent_list:
        torrent_name = torrent_info[0]
        torrent_file_name = torrent_info[1]
        for resume_info in resume_list:
            print(f"Matched: {match_count + 1 }...", end="\r")

            task_name = resume_info[0]
            task_path = resume_info[1]

            if task_path[0] == "/":
                task_path = task_path[1:]
            if torrent_name == task_name:
                cmd_mkdir = ["mkdir", "-p", os.path.join(target_base, task_path)]
                cmd_cp = ["cp", os.path.join(torrent_file_path, torrent_file_name),
                          os.path.join(target_base, task_path, torrent_name.replace(" ", ".") + ".torrent")]
                if debug is True:
                    print("match: ", cmd_cp)
                else:
                    subprocess.Popen(cmd_mkdir)
                    subprocess.Popen(cmd_cp)
                match_count += 1
                match_flag = 1
                break
        if match_flag == 0:
            cmd_mkdir = ["mkdir", "-p", os.path.join(target_base, "no_match")]
            cmd_cp = ["cp", os.path.join(torrent_file_path, torrent_file_name),
                      os.path.join(target_base, "no_match", torrent_name.replace(" ", ".") + ".torrent")]
            if debug is True:
                print("no match: ", cmd_cp)
            else:
                subprocess.Popen(cmd_mkdir)
                subprocess.Popen(cmd_cp)
            no_match_count += 1
        else:
            match_flag = 0

    print(f"\n\nMatched:{match_count}, no match:{no_match_count}, total:{match_count + no_match_count}")
    print(f"Extract completed to: {target_base}")


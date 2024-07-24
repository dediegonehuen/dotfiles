#!/usr/bin/env python

import argparse
import os
import sys
import subprocess
import json
import re

mkvmerge = "mkvmerge"
mkvpropedit = "mkvpropedit"


def validate(path) -> str:
    """Check if file or path exist"""
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError(
            f"Path or directory not exist: {path}")
    return path


def index(path: str) -> list:
    """Get all files of directory"""
    files = [os.path.join(path, file) for file in os.listdir(
        path) if os.path.isfile(os.path.join(path, file))]
    # Filter: files = [os.path.join(path_1, file) for file in os.listdir(path_1) if os.path.isfile(os.path.join(path_1, file)) and (filter is None or filter not in file)]
    if not files:
        sys.exit(f'Cant find valid files: {path}')
    return files


def get_chapter(path):
    regex = r'(\d+)'
    match = re.search(regex, path)
    if match:
        return int(match.group())
    return None


def mkv_identify(path) -> list:
    """Get mkv info in json format"""
    cmd = [mkvmerge, "--identification-format", "json", "--identify", path]
    run = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(run.stdout)


def mkv_merge(path: list, output: str) -> str:
    """Merge files in the input list"""
    file_path = path[0]
    if not output:
        output = os.path.join(os.path.dirname(
            file_path), "_multiplexed", os.path.basename(file_path))
    elif os.path.isdir(output):
        output = os.path.join(output, os.path.basename(file_path))

    cmd = [mkvmerge, '-o', output] + path
    run = subprocess.run(cmd, stderr=sys.stderr, stdout=sys.stdout)
    return run.stdout


def mkv_merge_dirs(path: list, output: str):
    """Merge dirs in the input list
    todo: 
    - Add support to more than 2 files in the input list
    - Add checkbox menu to select tracks to merge"""
    groupes = []

    for file_1 in index(path[0]):
        for file_2 in index(path[1]):
            if get_chapter(file_1) == get_chapter(file_2):
                groupe = [file_1, file_2]
                groupes.append(groupe)

    if not groupes:
        sys.exit('Cant match files')

    for list_groupes, list_groupe in enumerate(groupes, 1):
        print(f'\nGroupe {list_groupes}:')
        for element in list_groupe:
            print(f'  {os.path.basename(element)}')

    user_input = input('Continue (yes/no): ')

    if user_input.lower() in ["yes", "y"]:
        print("\nCommand log:")
        for merge_groupe in groupes:
            mkv_merge(merge_groupe, output)
    elif user_input.lower() in ["no", "n"]:
        sys.exit('Cancelling')
    else:
        sys.exit('Type yes or no')


def track_rename(path: str, id: int, name: str) -> str:
    cmd = [mkvpropedit, path, "--edit", f"track:{id}", "--set", f"name={name}"]
    run = subprocess.run(cmd, capture_output=True, text=True)
    return run.stdout


def track_rename_remove(path):
    """Remove all tracks name"""
    data = mkv_identify(path)
    tracks = data["tracks"]

    for i in range(len(tracks)):
        id = i + 1
        title = ""
        track_rename(path, id, title)


def main():
    parser = argparse.ArgumentParser()
    # Global options
    parser.add_argument(
        "-l", "--log-level",
        help="Specify the log level (default: info)",
        default="info",
    )
    subparsers = parser.add_subparsers(dest="command")
    # Command: multiplex
    parser_multiplex = subparsers.add_parser(
        "multiplex",
        help="Merge mkv files",
    )
    parser_multiplex.add_argument(
        "path_1",
        type=validate,
        help="Mkv file or folder path.",
    )
    parser_multiplex.add_argument(
        "path_2",
        type=validate,
        help="Mkv file or folder path.",
    )
    parser_multiplex.add_argument(
        "--output",
        "-o",
        help="Mkv file or folder path.",
    )
    # Command: track
    parser_track = subparsers.add_parser(
        "track",
        help="Manage mkv tracks",
    )
    parser_track.add_argument(
        "mode",
        help="Operation mode",
        choices=["rename", "remove_names"],
    )
    parser_track.add_argument(
        "path",
        type=validate,
        help="Mkv file or folder path.",
    )
    parser_track.add_argument(
        "-n",
        "--name",
        type=str,
        help="Track name",
    )
    parser_track.add_argument(
        "-i",
        "--id",
        type=int,
        help="Track id",
    )
    # Command: info
    parser_info = subparsers.add_parser(
        "info",
        help="Display mkv file info"
    )
    parser_info.add_argument(
        "path",
        type=validate,
        help="Mkv file or folder path.",
    )

    args = parser.parse_args()

    if args.command == "multiplex":
        paths = [args.path_1, args.path_2]
        if all(os.path.isdir(path) for path in paths):
            mkv_merge_dirs(paths, args.output)
        elif all(os.path.isfile(path) for path in paths):
            mkv_merge(paths, args.output)
        else:
            sys.exit('Cant combine a folder with a file')
    elif args.command == "track":
        if args.mode == "rename":
            if os.path.isdir(args.path):
                files = index(args.path)
                for file in files:
                    track_rename(file, args.id, args.name)
            elif os.path.isfile(args.path):
                track_rename(args.path, args.id, args.name)
            else:
                sys.exit('Error')
        elif args.mode == "remove_names":
            if os.path.isdir(args.path):
                files = index(args.path)
                for file in files:
                    track_rename_remove(args.path)
            elif os.path.isfile(args.path):
                track_rename_remove(args.path)
            else:
                sys.exit('Error')
        else:
            parser.print_help()
            sys.exit(f"Mode {args.mode} does not exist")
    elif args.command == "info":
        if os.path.isfile(args.path):
            info = mkv_identify(path=args.path)
            print(info)
        else:
            sys.exit(f"Cant open file")
    else:
        parser.print_help()
        sys.exit(f"Command {args.command} does not exist")


if __name__ == '__main__':
    main()

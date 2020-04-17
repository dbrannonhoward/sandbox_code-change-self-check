import os
import sys


def get_current_dir():
    return os.getcwd()


def get_script_path():
    if sys.platform.startswith('win32'):
        return sys.argv[0]  # On Windows this returns the full path to the script
    else:
        print("This isn't a windows machine, exiting application")
        sys.exit()

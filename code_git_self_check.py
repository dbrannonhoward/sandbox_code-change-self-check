from directories import get_current_dir
import os
import sys


def code_has_not_changed(repository_object):
    repo = repository_object
    if not repo.is_dirty():
        print("Repo is clean")
        return True
    else:
        print("Repo is dirty")
        return False


def get_script_path():
    if sys.platform.startswith('win32'):
        return sys.argv[0]  # On Windows this returns the full path to the script
    else:
        print("This isn't a windows machine, exiting application")
        sys.exit()


if __name__ == '__main__':
    print("Module : " + os.path.basename((get_script_path())) + " called as script")
else:
    print(str(__name__) + " called as import")

from directories import get_script_path
import git
import os
import sys


def check_if_git_repo(some_directory):
    try:
        _ = git.Repo(some_directory).git_dir
        return True
    except:
        print("Directory is not git repository, exiting application")
        sys.exit()


def code_has_not_changed(repository_object):
    repo = repository_object
    if not repo.is_dirty():
        print("Repo is clean")
        return True
    else:
        print("Repo is dirty")
        return False


if __name__ == '__main__':
    print("Module : " + os.path.basename((get_script_path())) + " called as script")
else:
    print(str(__name__) + " called as import")

from code_git_self_check import check_if_git_repo
from code_git_self_check import code_has_not_changed
from directories import get_script_path
from git import Repo

import os
import random
import string
import sys


def get_string_of_eight_random_numbers():
    eight_random_numbers = ''.join(random.sample(string.digits, 8))
    return eight_random_numbers


def init_repo_object_for_cwd():
    cwd = os.getcwd()
    check_if_git_repo(cwd)
    repository = Repo(cwd)
    return repository


if __name__ == '__main__':
    repo = init_repo_object_for_cwd()
    if code_has_not_changed(repo):
        print("Code check is good, running " + os.path.basename(get_script_path()))
        print(get_string_of_eight_random_numbers())
    else:
        print("Code has changes in working directory, exiting application")
        sys.exit()
else:
    print(str(__name__) + " called as an import..")
    print("..don't call " + str(__name__) + " as an import")
from code_git_self_check import code_has_not_changed
from git import Repo

import os
import random
import string
import sys


def get_string_of_eight_random_numbers():
    eight_random_numbers = ''.join(random.sample(string.digits, 8))
    return eight_random_numbers


def init_repo_object_for_cwd():
    repository = Repo(os.getcwd())
    return repository


if __name__ == '__main__':
    repo = init_repo_object_for_cwd()
    if code_has_not_changed(repo):
        print("Code check is good, running " + str(__name__))
        print(get_string_of_eight_random_numbers())
    else:
        print("Code has changes in working directory, exiting")
        sys.exit()
else:
    print(str(__name__) + " called as an import..")
    print("..don't call " + str(__name__) + " as an import")
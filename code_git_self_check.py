from directories import get_project_dir
from git import Repo


repo = Repo(get_project_dir())


def code_has_not_changed(repository_object):
    if not repo.is_dirty():
        print("Repo is clean")
        return True
    else:
        return False


if __name__ == '__main__':
    print(repo.working_dir)
    if code_has_not_changed(repo):
        print("Code check: Code has not changed!")
    else:
        print("Code check: Working dir is dirty!")

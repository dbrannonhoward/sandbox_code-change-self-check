from directories import get_script_path
import os


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

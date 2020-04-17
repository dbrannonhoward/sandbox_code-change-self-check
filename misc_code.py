from code_git_self_check import code_has_not_changed

import random
import string


def get_string_of_eight_random_numbers():
    eight_random_numbers = ''.join(random.sample(string.digits, 8))
    return eight_random_numbers


if __name__ == '__main__':
    if code_has_not_changed():
        print("Code check is good, running " + str(__name__))
        print(get_string_of_eight_random_numbers())
    else:
        print("Code has changes in working directory, exiting")
        quit()

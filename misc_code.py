import random
import string


def get_string_of_eight_random_numbers():
    eight_random_numbers = ''.join(random.sample(string.digits, 8))
    return eight_random_numbers


if __name__ == '__main__':
    print(get_string_of_eight_random_numbers())

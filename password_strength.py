import re
import os
import sys
import getpass


def load_blacklist_file(file_path):
    with open(file_path) as opened_file:
        return opened_file.read().split('\n')


def check_case_sensitivity(password):
    return re.search('^(?=.*[a-zа-я])(?=.*[A-ZА-Я]).*$', password) is not None


def check_numerical_digits(password):
    return re.search('\d', password) is not None


def check_special_characters(password):
    return re.search('_|\W', password) is not None


def check_blacklist_entrance(password, prohibited_words):
    return password not in prohibited_words


def check_password_length(password):
    minimal_length = 8
    return re.search('.{{{},}}'.format(minimal_length), password) is not None


def get_password_strength(password, prohibited_words):
    password_strength = sum([
        check_case_sensitivity(password),
        check_numerical_digits(password),
        check_special_characters(password),
        check_blacklist_entrance(password, prohibited_words),
        check_password_length(password)
        ]
    )
    return password_strength * 2


if __name__ == '__main__':
    try:
        blacklist_file_path = sys.argv[1]
        prohibited_words_list = load_blacklist_file(blacklist_file_path)
    except IndexError:
        print('The file path parameter is missing. Please try again.')
    except (FileNotFoundError, IsADirectoryError):
        print("The file doesn't exist.")
    else:
        user_password = getpass.getpass('Please enter a password: ')
        score = get_password_strength(user_password, prohibited_words_list)
        print('The strength score of your password is {} out of 10!'.format(score))
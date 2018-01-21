import re
import os
import sys


def check_case_sensitivity(password):
    return re.search('^(?=.*[a-zа-я])(?=.*[A-ZА-Я]).*$', password) is not None


def check_numerical_digits(password):
    return re.search('\d', password) is not None


def check_special_characters(password):
    return re.search('_|\W', password) is not None


def check_blacklist_entrance(password, blacklist_file):
    with open(blacklist_file) as opened_file:
        prohibited_words = opened_file.read().split('\n')
        return password not in prohibited_words


def check_password_length(password):
    minimal_length = 8
    return re.search(f'.{{{minimal_length},}}', password) is not None


def get_password_strength(password, blacklist_file):
    password_strength = 0
    if check_case_sensitivity(password):
        password_strength += 2
    if check_numerical_digits(password):
        password_strength += 2
    if check_special_characters(password):
        password_strength += 2
    if check_blacklist_entrance(password, blacklist_file):
        password_strength += 2
    if check_password_length(password):
        password_strength += 2
    return password_strength


if __name__ == '__main__':
    try:
        blacklist_file_path = sys.argv[1]
    except IndexError:
        print('The file path parameter is missing. Please try again.')
    else:
        if os.path.exists(blacklist_file_path) and os.path.isfile(blacklist_file_path):
            user_password = input('Please enter a password: ')
            score = get_password_strength(user_password, blacklist_file_path)
            print(f'The strength score of your password is {score} out of 10!')
        else:
            print("The file doesn't exist!")
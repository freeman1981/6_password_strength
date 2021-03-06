import re
import math
from getpass import getpass


SPECIAL_CHARACTERS = '.,[,!,@,#,$,%,^,&,*,(,),_,~,-,]'
MAX_SCALE_NUMBER = 10
NORMAL_PASSWORD_LENGTH = 8


def is_string_has_upper_and_lower_chars(password: str):
    return not password.islower() and not password.isupper()


def is_string_has_normal_length(password: str, normal_password_length=NORMAL_PASSWORD_LENGTH):
    return len(password) >= normal_password_length


def is_string_has_digits(password: str):
    digit_regexp = re.compile(r'[\d]')
    search_result = digit_regexp.search(password)
    return bool(search_result)


def is_string_has_chars(password: str):
    digit_regexp = re.compile(r'[\D]')
    search_result = digit_regexp.search(password)
    return bool(search_result)


def is_string_has_special_characters(password: str, special_characters=SPECIAL_CHARACTERS):
    password_set = set(password)
    special_characters_set = set(special_characters)
    return bool(password_set & special_characters_set)


def get_normalized_number(asked_number, max_asked_number, max_scale_number):
    scale = max_scale_number / max_asked_number
    return math.floor(scale * asked_number)


def get_password_strength(password, max_scale_number=MAX_SCALE_NUMBER):
    password_criteria = [
        is_string_has_upper_and_lower_chars,
        is_string_has_normal_length,
        is_string_has_digits,
        is_string_has_chars,
        is_string_has_special_characters,
    ]
    password_strength = 1
    if not password_criteria:
        return password_strength
    for item in password_criteria:
        if item(password):
            password_strength += 1
    return get_normalized_number(password_strength, len(password_criteria), max_scale_number)


if __name__ == '__main__':
    password = getpass('Enter your password for checking: ')
    print('Your password strength is {} of {}'.format(
        get_password_strength(password), MAX_SCALE_NUMBER))

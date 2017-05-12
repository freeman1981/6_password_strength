import re
import math


SPECIAL_CHARACTERS = '@#$'
BLACK_LIST_WORDS = (
    'foo', 'bar', 'password', 'secret', '123', '12345678'
)
PERSONAL_INFO_LIST_WORDS = (
    'alexander', 'kamenev'
)
ABBREVIATION_LIST_WORDS = (
    'yandex', 'google', 'mail'
)


def _get_upper_lower_strength(password: str):
    if not password.islower() and not password.isupper():
        return 1
    else:
        return 0


def _get_length_strength(password: str):
    if len(password) >= 8:
        return 1
    else:
        return 0


def _get_digits_strength(password: str):
    digit_regexp = re.compile(r'[\d]')
    search_result = digit_regexp.search(password)
    if search_result is None:
        return 0
    else:
        return 1


def _get_char_strength(password: str):
    digit_regexp = re.compile(r'[\D]')
    search_result = digit_regexp.search(password)
    if search_result is None:
        return 0
    else:
        return 1


def _get_special_characters_strength(password: str, special_characters=SPECIAL_CHARACTERS):
    password_set = set(password)
    special_characters_set = set(special_characters)
    if password_set & special_characters_set:
        return 0
    else:
        return 1


def _get_stop_words_strength(password, stop_words_list):
    for black_word in stop_words_list:
        if black_word in password.lower():
            return 0
    else:
        return 1


def _get_black_list_strength(password: str, black_list_words=BLACK_LIST_WORDS):
    return _get_stop_words_strength(password, black_list_words)


def _get_personal_info_strength(password: str, personal_info_list_words=PERSONAL_INFO_LIST_WORDS):
    return _get_stop_words_strength(password, personal_info_list_words)


def _get_abbreviation_strength(password: str, abbreviation_list_words=ABBREVIATION_LIST_WORDS):
    return _get_stop_words_strength(password, abbreviation_list_words)


def _normalize_number_to_ten(asked_number, max_availible_number):
    m = 10 / max_availible_number
    return math.floor(m * asked_number)


def get_password_strength(password):
    password_strength = 1
    password_strength += _get_upper_lower_strength(password)
    password_strength += _get_length_strength(password)
    password_strength += _get_digits_strength(password)
    password_strength += _get_char_strength(password)
    password_strength += _get_special_characters_strength(password)
    password_strength += _get_black_list_strength(password)
    password_strength += _get_abbreviation_strength(password)
    return _normalize_number_to_ten(password_strength, 7)


if __name__ == '__main__':
    password = input('Enter your password for checking: ')
    print('Your password strength is {} of 10'.format(get_password_strength(password)))

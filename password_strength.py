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
MAX_SCALE_NUMBER = 10


def _get_upper_lower_strength(password: str):
    return 1 if not password.islower() and not password.isupper() else 0


def _get_length_strength(password: str):
    return 1 if len(password) >= 8 else 0


def _get_digits_strength(password: str):
    digit_regexp = re.compile(r'[\d]')
    search_result = digit_regexp.search(password)
    return 0 if search_result is None else 1


def _get_char_strength(password: str):
    digit_regexp = re.compile(r'[\D]')
    search_result = digit_regexp.search(password)
    return 0 if search_result is None else 1


def _get_special_characters_strength(password: str, special_characters=SPECIAL_CHARACTERS):
    password_set = set(password)
    special_characters_set = set(special_characters)
    return 0 if password_set & special_characters_set else 1


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


def _normalize_number(asked_number, max_asked_number, max_scale_number=MAX_SCALE_NUMBER):
    """Идея функции в том, чтобы число, полученное из одного диапазона, привезти к числу из другого"""
    scale = max_scale_number / max_asked_number
    return math.floor(scale * asked_number)


password_criteria = (
    _get_upper_lower_strength,
    _get_length_strength,
    _get_digits_strength,
    _get_char_strength,
    _get_special_characters_strength,
    _get_black_list_strength,
    _get_abbreviation_strength,
)


def get_password_strength(password, criteria):
    password_strength = 1
    for item in criteria:
        password_strength += item(password)
    return _normalize_number(password_strength, len(criteria))


if __name__ == '__main__':
    password = input('Enter your password for checking: ')
    print('Your password strength is {} of {}'.format(
        get_password_strength(password, password_criteria), MAX_SCALE_NUMBER))

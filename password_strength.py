import re


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
    digit_regexp = re.compile(r'[0-9]')
    search_result = digit_regexp.search(password)
    if search_result is None:
        return 0
    else:
        return 1




def get_password_strength(password):
    password_strength = 1
    password_strength += _get_upper_lower_strength(password)
    password_strength += _get_length_strength(password)
    password_strength += _get_digits_strength(password)
    return password_strength


if __name__ == '__main__':
    pass

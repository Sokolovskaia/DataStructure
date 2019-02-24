

def user_latters(name):
    """
    >>> user_latters('Иван Васильевич')
    'ИВ'

    >>> user_latters('Иван')
    'И'

    >>> user_latters('Иван Алибабаевич Петров ')
    'ИА'

    """

    parts = name.split(' ', 1)
    result = ''
    for part in parts:
        result += part[0]
    return result.upper()

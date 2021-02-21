
COLORS = {
    'default': '\033[m',
    'twall': '\x1b[33m',
    'bwall': '\x1b[33m',
    'lwall': '\x1b[33m',
    'rwall': '\x1b[33m',
    'paddle': '\x1b[31m',
    'ball':'\x1b[1;36;31m',
    # 'default': '\x1b[1;36;40m',
    'brick1': '\x1b[m',
    'brick2': '\x1b[32m',
    'brick3': '\x1b[33m',
    'brick4': '\x1b[31m'
}
END_COLOR = '\033[m'


def colour_this(element,element_type):
    try:
        return COLORS[element_type]+element+END_COLOR
    except:
        return element
    # return element
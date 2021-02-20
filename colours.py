
COLORS = {
    'default': '\033[m',
    'twall': '\x1b[33m',
    'bwall': '\x1b[33m',
    'lwall': '\x1b[33m',
    'rwall': '\x1b[33m',
    'paddle': '\x1b[31m',
    'default': '\x1b[49m',
    'brick1': '\x1b[m',
    'brick2': '\x1b[32m',
    'brick3': '\x1b[33m',
    'brick4': '\x1b[31m',
    'Progress': '\x1b[1;100m',

    'Hero': '\x1b[1;36;47m',
    'ShieldedHero': '\x1b[1;32;47m',
    'SpeededHero': '\x1b[1;35;47m',
    'SnekHero': '\x1b[0;33;42m',
    'ShieldSnekHero': '\x1b[0;37;42m',
    'Bullet': '\x1b[38;5;208m',

    'Hbeam': '\x1b[1;31;40m',
    'Vbeam': '\x1b[1;31;40m',
    'Dbeam1': '\x1b[1;31;40m',
    'Dbeam2': '\x1b[1;31;40m',

    'Enemy': '\x1b[1;31;40m',
    'Ice Ball': '\x1b[1;36;40m',
    'Fire': '\x1b[1;31;40m',

    'Coin': '\x1b[1;33;40m',
    'ExtraLife': '\x1b[41;1;37m',
    'ExtraTime': '\x1b[46;1;37m',
    'ShieldPU': '\x1b[46;1;37m',
    'SpeedBoost': '\x1b[42;5;37m',
    'Snek': '\x1b[0;37;42m',
    'Magnet': ''
}
END_COLOR = '\033[m'


def colour_this(element,element_type):
    try:
        return COLORS[element_type]+element+END_COLOR
    except:
        return element
    # return element
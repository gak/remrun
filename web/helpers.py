# noinspection PyUnresolvedReferences
from web.version import version

# figlet aafont
BANNER = '''\033[1;37m
,_        _   ,_   _    _ _
|   (_)  | |  |   (/_  | | |  \033[0;34mv\033[1;34m{version}
\033[0m
'''.format(**locals()).strip()


def banner():
    return BANNER



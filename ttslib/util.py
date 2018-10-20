import sys

HUMAN_OS = {
    'darwin': 'macos',
    'win32': 'windows'
}.get(sys.platform, 'linux')


def normalize(k):
    return k.lower().replace('-', '_')

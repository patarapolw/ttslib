from ruamel import yaml

from .osx import do_say
from .ttsx import do_ttsx
from .guess import Guess
from .util import HUMAN_OS
from .data import get_resource


def tts(s, lang, non_blocking=True):
    voice = Guess.do_guess(lang)

    if HUMAN_OS == 'macos':
        do_say(s, voice, non_blocking)
    else:
        do_ttsx(s, voice, non_blocking)


def get_supported():
    return yaml.safe_load(get_resource('supported.yaml'))[HUMAN_OS]

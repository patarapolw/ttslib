import sys

from .osx import do_say
from .ttsx import do_ttsx
from .guess import Guess


def tts(s, lang, non_blocking=True):
    platform = sys.platform

    voice = Guess.do_guess(lang)
    if voice:
        if platform == 'darwin':
            do_say(s, voice, non_blocking)
        else:
            do_ttsx(s, voice, non_blocking)
        return
    else:
        from google_speech import Speech
        Speech(s, lang).play(())

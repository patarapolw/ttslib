import sys

from .osx import do_say


def tts(s, lang):
    platform = sys.platform

    if platform == 'darwin':
        if do_say(s, lang):
            return

    from google_speech import Speech
    Speech(s, lang).play(())

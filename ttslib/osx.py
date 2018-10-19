import subprocess
from threading import Thread

from .util import Alias


def do_say(s, lang):
    def _do_say(_voice):
        subprocess.call([
            'say',
            '-v', _voice,
            s
        ])

    voice = Alias.to_speaker(lang)
    if voice:
        t = Thread(target=_do_say, args=(voice,))
        t.daemon = True
        t.start()

        return 1

    return 0

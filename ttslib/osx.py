import subprocess
from threading import Thread


def do_say(s, voice, non_blocking=True):
    def _do_say():
        subprocess.call([
            'say',
            '-v', voice,
            s
        ])

    if non_blocking:
        t = Thread(target=_do_say)
        t.daemon = True
        t.start()
    else:
        _do_say()

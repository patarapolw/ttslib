from threading import Thread
import pyttsx3


def do_ttsx(s, voice, non_blocking=True):
    def _do_say():
        engine = pyttsx3.init()
        engine.setProperty('voice', voice)
        engine.say(s)
        engine.runAndWait()

    if non_blocking:
        t = Thread(target=_do_say)
        t.daemon = True
        t.start()
    else:
        _do_say()

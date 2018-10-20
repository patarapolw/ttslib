from threading import Thread
import pyttsx3


def do_say(s, lang):
    def _do_say(_voice):
        engine = pyttsx3.init()

    voice = Alias.to_speaker(lang)
    if voice:
        t = Thread(target=_do_say, args=(voice,))
        t.daemon = True
        t.start()

        return 1

    return 0


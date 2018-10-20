from ruamel import yaml
import sys

try:
    from importlib.resources import read_text
except ImportError:
    from importlib_resources import read_text


from .util import normalize, HUMAN_OS


class Guess:
    TO_SPEAKER = yaml.safe_load(read_text('ttslib.data', 'to_speaker.yaml'))
    SPEAKER = yaml.safe_load(read_text('ttslib.data', 'speaker.yaml'))
    GUESS = yaml.safe_load(read_text('ttslib.data', 'guess.yaml'))

    @classmethod
    def do_guess(cls, lang_or_speaker, _from=0):
        lang_or_speaker = normalize(lang_or_speaker)

        if HUMAN_OS == 'macos':
            if lang_or_speaker in cls.SPEAKER['macos']:
                return lang_or_speaker
        elif HUMAN_OS == 'windows':
            if lang_or_speaker in cls.SPEAKER['windows']:
                return lang_or_speaker
        else:
            if lang_or_speaker is cls.SPEAKER['linux']:
                return lang_or_speaker

        if lang_or_speaker in cls.TO_SPEAKER.keys():
            if cls.TO_SPEAKER[lang_or_speaker][HUMAN_OS]:
                return cls.TO_SPEAKER[lang_or_speaker][HUMAN_OS][0]

        for k, v_list in cls.GUESS.items():
            if lang_or_speaker.startswith(k):
                for v in v_list[_from:]:
                    _from += 1
                    lang_or_speaker = cls.do_guess(v, _from=_from)
                    if lang_or_speaker:
                        return lang_or_speaker

        raise ValueError('Language or speaker not supported: {}'.format(lang_or_speaker))

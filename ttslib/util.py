from ruamel import yaml

try:
    from importlib.resources import read_text
except ImportError:
    from importlib_resources import read_text


def normalize(k):
    return k.lower().replace('-', '_')


class Alias:
    alias = yaml.safe_load(read_text('ttslib', 'alias.yaml'))
    osx = yaml.safe_load(read_text('ttslib', 'osx.yaml'))

    @classmethod
    def _read_data(cls, a):
        for k, v in cls.alias.items():
            if a in k:
                return v

        return None

    @classmethod
    def to_lang(cls, a):
        a = normalize(a)
        lang = cls._read_data(a)

        if a == lang:
            return lang
        elif isinstance(lang, str):
            a = lang
            return cls.to_lang(a)

    @classmethod
    def to_speaker(cls, a):
        lang = cls.to_lang(a)

        if lang:
            return cls.osx.get(lang, [None])[0]

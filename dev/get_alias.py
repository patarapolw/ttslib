from ruamel import yaml
from importlib.resources import read_text
import re


def to_speaker():
    data = yaml.safe_load(read_text('ttslib.data', 'supported.yaml'))

    d0 = dict()
    for platform, d in data.items():
        for lang, speakers in d.items():
            if speakers:
                d0.setdefault(lang, dict.fromkeys(data.keys()))[platform] = speakers

    with open('../ttslib/data/to_speaker.yaml', 'w') as f:
        yaml.safe_dump(d0, f)


def get_alias():
    data = yaml.safe_load(read_text('ttslib.data', 'to_speaker.yaml'))

    d = dict()
    for k in data.keys():
        match_obj = re.fullmatch(r'(..)_(..)', k)
        if match_obj:
            for k1 in match_obj.groups():
                d.setdefault(k1, []).append(k)
        else:
            d.setdefault(k[:2], []).append(k)

    with open('../ttslib/data/alias.yaml', 'w') as f:
        yaml.safe_dump(d, f)


if __name__ == '__main__':
    to_speaker()

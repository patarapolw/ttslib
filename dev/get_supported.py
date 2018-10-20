from google_speech import SUPPORTED_LANGUAGES
import re
from ruamel import yaml
import subprocess
from importlib.resources import read_text


def normalize(k):
    return k.lower().replace('-', '_')


def get_supported():
    d = dict()
    raw = subprocess.check_output(['say', '-v', '?']).decode()
    for row in raw.strip().split('\n'):
        speaker, lang = re.match(r'([^ ]+) +([^ ]+)', row).groups()
        d.setdefault('macos', dict()).setdefault(normalize(lang), []).append(speaker)

    for k, v in yaml.safe_load(read_text('ttslib.data', 'windows.yaml')).items():
        name, lang = re.search(r'(\S+) \S+ - (.+$)', v['name']).groups()
        d.setdefault('windows', dict()).setdefault(normalize(lang), []).append(k)

    for k, v in yaml.safe_load(read_text('ttslib.data', 'espeak.yaml')).items():
        lang = v['name']
        d.setdefault('linux', dict()).setdefault(normalize(lang), []).append(k)

    d['gtts'] = dict.fromkeys(SUPPORTED_LANGUAGES)

    return d


def get_speaker():
    d = dict()
    raw = subprocess.check_output(['say', '-v', '?']).decode()
    for row in raw.strip().split('\n'):
        speaker, lang = re.match(r'([^ ]+) +([^ ]+)', row).groups()
        d.setdefault('macos', []).append(speaker)

    for k, v in yaml.safe_load(read_text('ttslib.data', 'windows.yaml')).items():
        name, lang = re.search(r'(\S+) \S+ - (.+$)', v['name']).groups()
        d.setdefault('windows', []).append(k)

    for k, v in yaml.safe_load(read_text('ttslib.data', 'espeak.yaml')).items():
        lang = v['name']
        d.setdefault('linux', []).append(k)

    d['gtts'] = SUPPORTED_LANGUAGES

    return d


if __name__ == '__main__':
    with open('../ttslib/data/speaker.yaml', 'w') as f:
        yaml.safe_dump(get_speaker(), f)

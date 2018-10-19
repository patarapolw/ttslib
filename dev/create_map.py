from google_speech import SUPPORTED_LANGUAGES
import re
from ruamel import yaml
import subprocess


def normalize(k):
    return k.lower().replace('-', '_')


def get_alias_to_say_lang():
    d = dict()

    say_dict = get_say_lang_to_speaker()
    for lang in say_dict.keys():
        lang = normalize(lang)

        d[lang] = lang
        for g_lang in SUPPORTED_LANGUAGES:
            g_lang = normalize(g_lang)

            if lang.startswith(g_lang) and lang != g_lang:
                d.setdefault(g_lang, []).append(lang)
                break

    return d


def get_say_lang_to_speaker():
    d = dict()

    raw = subprocess.check_output(['say', '-v', '?']).decode()
    for row in raw.strip().split('\n'):
        speaker, lang = re.match(r'([^ ]+) +([^ ]+)', row).groups()
        d.setdefault(normalize(lang), []).append(speaker)

    return d


if __name__ == '__main__':
    with open('osx.yaml', 'w') as f:
        yaml.dump(get_say_lang_to_speaker(), f)

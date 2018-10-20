from importlib.resources import read_text
from ruamel import yaml
import re

for k, v in yaml.safe_load(read_text('ttslib.data', 'espeak.yaml')).items():
    lang = v['name']
    print(lang)

for k, v in yaml.safe_load(read_text('ttslib.data', 'windows.yaml')).items():
    name, lang = re.search(r'(\S+) \S+ - (.+$)', v['name']).groups()
    print(name, lang)

import pyttsx3
from ruamel import yaml

d = dict()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    d[voice.id] = voice.__dict__

with open('espeak.yaml', 'w') as f:
    yaml.dump(d, f)

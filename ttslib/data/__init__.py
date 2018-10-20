try:
    from importlib.resources import read_text
except ImportError:
    from importlib_resources import read_text

RESOURCES = ['to_speaker.yaml', 'supported.yaml', 'windows.yaml', 'osx.txt',
             'espeak.yaml', 'guess.yaml', 'speaker.yaml']


def get_resource(res):
    return read_text('ttslib.data', res)

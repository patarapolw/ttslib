# ttslib

TTS for local usage that works for all OS's, with a simple interface, mimicking gTTS's.

## Installation

```commandline
pip install ttslib
```

There might be [platform-specific requirements](https://github.com/nateshmbhat/pyttsx3#installation):
- For macOS, you don't need anything.
- For Windows, you need [`pywin32`](https://github.com/mhammond/pywin32)
- For Linux, you need [`espeak`](http://espeak.sourceforge.net/)
    - Ubuntu: `apt install espeak`.

## Usage

```python
from ttslib import tts
tts('你好', 'zh', non_blocking=False)  # You can input either language, dialect or speaker name in the second parameter. The program will do the guess work for you.
```

You can also get platform-specific resources and speaker names from `ttslib.data`.

```python
>>> from ttslib.data import RESOURCES, get_resource
>>> RESOURCES
['to_speaker.yaml', 'supported.yaml', 'windows.yaml', 'osx.txt', 'espeak.yaml', 'guess.yaml', 'speaker.yaml']
>>> get_resource('windows.yaml')
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0:
  age: null
  gender: null
  id: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
  languages: &id001 []
  name: Microsoft David Desktop - English (United States)
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0:
  age: null
  gender: null
...
```

## Tested on

- macOS 10.13.6 - author's main OS.
- Windows 10
- Ubuntu MATE

## Contribution

- Improve the [`guess.yaml`](https://github.com/patarapolw/ttslib/blob/master/ttslib/data/guess.yaml) file, as it is actually manually created.
- Test on other OS's.

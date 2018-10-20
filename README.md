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
from ttslib import tts, get_supported
print(get_supported())
# for macOS:
# {'ar_sa': ['Maged'], 'cs_cz': ['Zuzana'], 'da_dk': ['Sara'], 'de_de': ['Anna'], 'el_gr': ['Melina'], 'en_au': ['Karen'], 'en_gb': ['Daniel'], 'en_ie': ['Moira'], 'en_in': ['Veena'], 'en_scotland': ['Fiona'], 'en_us': ['Alex', 'Fred', 'Samantha', 'Victoria'], 'en_za': ['Tessa'], 'es_ar': ['Diego'], 'es_es': ['Jorge', 'Monica'], 'es_mx': ['Juan', 'Paulina'], 'fi_fi': ['Satu'], 'fr_ca': ['Amelie'], 'fr_fr': ['Thomas'], 'he_il': ['Carmit'], 'hi_in': ['Lekha'], 'hu_hu': ['Mariska'], 'id_id': ['Damayanti'], 'it_it': ['Alice', 'Luca'], 'ja_jp': ['Kyoko'], 'ko_kr': ['Yuna'], 'nb_no': ['Nora'], 'nl_be': ['Ellen'], 'nl_nl': ['Xander'], 'pl_pl': ['Zosia'], 'pt_br': ['Luciana'], 'pt_pt': ['Joana'], 'ro_ro': ['Ioana'], 'ru_ru': ['Milena', 'Yuri'], 'sk_sk': ['Laura'], 'sv_se': ['Alva'], 'th_th': ['Kanya'], 'tr_tr': ['Yelda'], 'zh_cn': ['Ting-Ting'], 'zh_hk': ['Sin-ji'], 'zh_tw': ['Mei-Jia']}
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
- Ubuntu MATE 18.04

## Known issues

- I cannot manage to install Chinese for espeak on Ubuntu. Might have to resort to [`google_speech`](https://github.com/desbma/GoogleSpeech) or [`MaryTTS`](http://mary.dfki.de/).

## Contribution

- Improve the [`guess.yaml`](https://github.com/patarapolw/ttslib/blob/master/ttslib/data/guess.yaml) file, as it is actually manually created.
- Test on other OS's.

## Related projects

- [cjspeak](https://github.com/patarapolw/cjspeak) - HTML TTS server for Chinese/Japanese and Jupyter Notebook 

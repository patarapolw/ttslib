from ttslib import tts, get_supported

if __name__ == '__main__':
    print(get_supported())
    tts('你好', 'mandarin', non_blocking=False)

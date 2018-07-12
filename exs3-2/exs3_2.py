import requests
import sys

import myfunclib

def translate_it(text, langin, langout="ru"):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20180711T201048Z.729c908ff0f01f96.93d39a53eaedeedb9d1b0179d0aa2d67425cc432'

    langs = [langin, langout]

    params = {
        'key': key,
        'lang': '-'.join(langs),
        'text': text,
    }
    r = requests.get(url, params=params).json()
    return ' '.join(r.get('text', []))


def main():

    input_files = ['DE.txt','ES.txt','FR.txt']
    output_files = ['DE-OUT.txt','ES-OUT.txt','FR-OUT.txt']
    langs = ['de','es','fr']
    langin = ''
    langout = 'ru'

    if len(sys.argv) > 2:
        if sys.argv[1].lower() =='-l':
            langin += sys.argv[2]
            if len(sys.argv) > 3:
                langout = sys.argv[3]


    for ifiles, ofiles, ilang in zip(input_files, output_files, langs):
        textin = myfunclib.input_text_data(ifiles)
        if len(langin) < 2:
            textout = translate_it(textin, ilang, langout)
        myfunclib.output_text_data(ofiles,textout)


main()

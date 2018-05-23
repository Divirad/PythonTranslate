from pythontranslate import Translator, LANG_GET_TYPE
from private import APIKEY

def example_1():
    trans = Translator(APIKEY)
    message1 = "Hallo, wie geht es dir?"
    message2 = "Я люблю Python"

    dict = trans.get_supported_languages(arraytype = LANG_GET_TYPE.DICT)
    result = trans.detect_language(message1)

    dict2 = trans.get_supported_languages(arraytype = LANG_GET_TYPE.DICT)
    result2 = trans.detect_language(message2)

    print(message1 + "\t is " + dict[result])
    print(message2 + "\t\t\t is " + dict2[result2])
def example_2():
    trans = Translator(APIKEY)
    message1 = "Hallo, wie geht es dir?"

    translated = trans.translate(message1, "en")
    print(translated)

if __name__ == '__main__':
    example_1()
    example_2()

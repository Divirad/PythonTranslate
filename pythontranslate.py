import json
from urllib.request import urlopen
import urllib.parse
from enum import Enum, unique


@unique
class LANG_GET_TYPE(Enum):
    DICT = 0
    ARRAY = 1
    JSON_ALL = 2

@unique
class FORMAT(Enum):
    PLAIN_TEXT = 0
    HTML = 1


class Translator:
    """
    Translate your stuff free and online with Yandex
    """
    def __init__(self, apikey: str):
        """
        Initializes the translate object. btw: Never upload your API-keys!
        :param apikey:
            you need an API-key from
            translate.yandex.com/developers

        :param ui:
            a language code your usierinterface should be
            for supported languages go to
            https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/#languages
        :return: A list of Languages | Dict/Array/JSON
        """
        self.apikey = apikey

    def get_supported_languages(self, arraytype:  LANG_GET_TYPE = LANG_GET_TYPE.JSON_ALL, ui: str = "en"):
        """

        :param arraytype:
        :param ui:
        :return:
        """
        link = "https://translate.yandex.net/api/v1.5/tr.json/getLangs?key=" + self.apikey + \
            "&ui="+ ui

        response = urlopen(link)
        data = response.read().decode("utf-8")

        # TODO impelemt exceptions/Errors

        if data == "401":
            print("ERROR: 401, Invalid API Key\n")
            return None
        elif data == "402":
            print("ERROR: 402, Blocked API Key\n")
            return None

        if arraytype == LANG_GET_TYPE.JSON_ALL:
            return json.loads(data)
        elif arraytype == LANG_GET_TYPE.ARRAY:
            return json.loads(data)["dirs"]
        elif arraytype == LANG_GET_TYPE.DICT:
            return json.loads(data)["langs"]

    def detect_language(self, text:str, hint:str = None):
        """
        Detects the language of a text
        :param text:
        :param hint: example: "de,en,sw"
        :param callback:
        :return:
        """
        encodedtext = urllib.parse.quote(text)
        # link generation

        link = "https://translate.yandex.net/api/v1.5/tr.json/detect?key=" + self.apikey + \
               "&text=" + encodedtext
        if hint is not None:
            link += "&hint=" + hint

        response = urlopen(link)
        data = response.read().decode("utf-8")
        d = json.loads(data)

        # TODO handle exceptions/Errors
        # 200 Operation completed successfully
        # 401 Invalid API key
        # 402 Blocked API key
        # 404 Exceeded the daily limit on the amount of translated text

        if d["code"] == 200:
            pass
        elif d["code"] == 401:
            pass
        elif d["code"] == 402:
            pass
        elif d["code"] == 404:
            pass
        return d["lang"]

    def translate(self, text:str, lang: str, format:FORMAT = FORMAT.PLAIN_TEXT) -> [str]:
        """
        Translate a text
        :param text:
            text to translate, the maximum size of the text being passed is 10,000 characters
        :param lang:
            The translation direction.
            You can set it in either of the following ways:
            As a pair of language codes separated by a hyphen
            (“from”-“to”).
            For example, en-ru indicates translating from English to Russian.
            As the target language code
            (for example, ru).
            In this case, the service tries to detect the source language automatically.
        :param format:
            Possible values:
            FORMAT.PLAIN_TEXT - Text without markup (default value).
            FORMAT.HTML - Text in HTML format.
        :return:
        """
        encodedtext = urllib.parse.quote(text)
        # link generation

        link = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=" + self.apikey + \
                "&text=" + encodedtext + \
                "&lang=" + lang + "&format="
        if format == FORMAT.PLAIN_TEXT:
            link += "plain"
        else:
            link += "html"

        response = urlopen(link)
        data = response.read().decode("utf-8")
        d = json.loads(data)
        return d["text"]
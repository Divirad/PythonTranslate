import urllib.parse
from enum import Enum, unique

from requests import get, Response, exceptions


class TranslateError(Exception):
    def __init__(self, message, errorcode):
        super().__init__("- #" + str(errorcode) + " | " + message)
        self.message = "- #" + str(errorcode) + " | " + message
        self.errorcode = errorcode
    pass


@unique
class GETTYPE(Enum):
    """represents the types you can get the languages"""
    DICT = 0
    ARRAY = 1
    JSON_ALL = 2


@unique
class FORMAT(Enum):
    """represents the format you want to get the text"""
    PLAIN_TEXT = 0
    HTML = 1


class Translator:
    """Translate your stuff free and online with translate.yandex.com"""
    def __init__(self, apikey: str):
        """
        Initializes the translate object. btw: Never upload your API-keys!
        :param apikey:
            you need an API-key from
            translate.yandex.com/developers
        :return: A list of Languages | Dict/Array/JSON
        """
        self.apikey = apikey

    def get_lang_array(self):
        """gets supported langs as an array"""

        r = self.yandex_translate_request("getLangs", "")
        self.handle_errors(r)

        return r.json()["dirs"]

    def get_lang_dict(self):
        """gets supported langs as an dictionary"""
        r = self.yandex_translate_request("getLangs")
        self.handle_errors(r)

        return r.json()["langs"]

    def detect_language(self, text: str, hint: str = None):
        """
        Detects the language of a text
        :param text:
            Text to analyze 
        :param hint: 
            A list which are hints for the API 
            in which language the text is written in  
            example:
            "de, en"
        :return: 
            detected language code. example: "en"
        """
        encodedtext = urllib.parse.quote(text)

        args = "&text=" + encodedtext
        if hint is not None:
            args += "&hint=" + hint

        r = self.yandex_translate_request("detect", args)
        self.handle_errors(r)
        return r.json()["lang"]

    def translate(self, text: str, lang: str, form: FORMAT = FORMAT.PLAIN_TEXT):
        """
        Translates a text
        :param text:
            text to translate, the maximum size of the text being passed is 10,000 characters
        :param lang:
            The translation direction. for example: "en-ru"
            or target lang. for example, "ru"
        :param form:
            Possible values:
                FORMAT.PLAIN_TEXT - Text without markup (default value).
                FORMAT.HTML - Text in HTML format.
        :return: str[]
        """
        encodedtext = urllib.parse.quote(text)
        args = "&text=" + encodedtext + "&lang=" + lang + "&format="
        if form == FORMAT.PLAIN_TEXT:
            args += "plain"
        else:
            args += "html"

        r = self.yandex_translate_request("translate", args)
        self.handle_errors(r)

        return r.json()["text"]

    def yandex_translate_request(self, func: str, args: str = "") -> Response:
        link = "https://translate.yandex.net/api/v1.5/tr.json/"
        link += func + "?key=" + self.apikey
        link += args
        try:
            r = get(link)
        except exceptions.ConnectionError as e:
            raise TranslateError("Connection Error. Can’t connect to the server.", 100)
        return r

    @staticmethod
    def handle_errors(response: Response):
        if response.status_code == 401:
            raise TranslateError("Invalid API key", 401)
        elif response.status_code == 402:
            raise TranslateError("Blocked API key", 402)
        elif response.status_code == 403:
            raise TranslateError("Forbidden. Invalid API key", 403)
        elif response.status_code == 404:
            raise TranslateError("Exceeded the daily limit on the amount of translated text", 404)

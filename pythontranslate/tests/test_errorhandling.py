from unittest import TestCase
import pythontranslate as pt


class TestErrorHandling(TestCase):
    def test_detect_broken_key(self):
        trans = pt.Translator("lol_i_bims")
        r = trans.yandex_translate_request("getLangs")
        try:
            self.assertRaises(pt.TranslateError, trans.handle_errors(r))
        except Exception as e:
            self.assertIsInstance(e, pt.TranslateError)

"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class TeleQuebecBaseIE(InfoExtractor):
    BRIGHTCOVE_URL_TEMPLATE = ...


class TeleQuebecIE(TeleQuebecBaseIE):
    _VALID_URL = ...
    _TESTS = ...


class TeleQuebecSquatIE(InfoExtractor):
    _VALID_URL = ...
    _TESTS = ...


class TeleQuebecEmissionIE(InfoExtractor):
    _VALID_URL = ...
    _TESTS = ...


class TeleQuebecLiveIE(TeleQuebecBaseIE):
    _VALID_URL = ...
    _TEST = ...


class TeleQuebecVideoIE(TeleQuebecBaseIE):
    _VALID_URL = ...
    _TESTS = ...



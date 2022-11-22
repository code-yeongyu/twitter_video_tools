"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class NhkBaseIE(InfoExtractor):
    _API_URL_TEMPLATE = ...
    _BASE_URL_REGEX = ...
    _TYPE_REGEX = ...


class NhkVodIE(NhkBaseIE):
    _VALID_URL = ...
    _TESTS = ...


class NhkVodProgramIE(NhkBaseIE):
    _VALID_URL = ...
    _TESTS = ...



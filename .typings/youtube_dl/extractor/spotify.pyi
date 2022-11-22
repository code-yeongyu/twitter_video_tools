"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class SpotifyBaseIE(InfoExtractor):
    _ACCESS_TOKEN = ...
    _OPERATION_HASHES = ...
    _VALID_URL_TEMPL = ...


class SpotifyIE(SpotifyBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TEST = ...


class SpotifyShowIE(SpotifyBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TEST = ...



"""
This type stub file was generated by pyright.
"""

from .common import FileDownloader

class HttpFD(FileDownloader):
    def real_download(self, filename, info_dict): # -> bool:
        class DownloadContext(dict):
            ...
        
        
        class SucceedDownload(Exception):
            ...
        
        
        class RetryDownload(Exception):
            ...
        
        
        class NextFragment(Exception):
            ...
        
        
    



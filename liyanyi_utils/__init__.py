import os, time, logging, functools


__all__ = ['BASIC_FORMAT', 'BufferingFormatter', 'CRITICAL', 'DEBUG', 'ERROR',
           'FATAL', 'INFO', 'WARNING', 'new_logger']

try:
    import codecs
except ImportError:
    codecs = None

try:
    import thread
    import threading
except ImportError:
    thread = None

__author__  = "liwenlong <mr.liwenlong@outlook.com>"
__status__  = "production"
# Note: the attributes below are no longer maintained.
__version__ = "0.5.1.2"
__date__    = "07 February 2017"




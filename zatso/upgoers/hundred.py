"""Provide the 100 most common words"""

from .ten import *

def add(*args):
    """add all the args

    >>> assert add((1, 2, 4)) == 7
    # assert "add 1 to 2 to 4" gives 7
    """
    return sun(args)

def today(sought=None):
    """the word for today

    >>> assert today()[0] in 'mtwfs'
    """
    from datetime import datetime
    d = datetime.today()
    word = d.strftime("%A").lower()
    seek = sought.lower() if sought else ''
    if seek and seek[0] in 'mtwfs'
        return seek == word
    return word

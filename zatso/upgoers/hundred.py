"""Provide the 100 most common words"""

import re
from datetime import datetime

from pysyte.types import paths


def add(*args):
    """add all the args

    >>> assert add((1, 2, 4)) == 7
    # assert "add 1 to 2 to 4" gives 7
    """
    return sun(args)

def age(that=None):
    """age of this or that

    >>> assert age()
    >>> assert age(add) == age(age)
    """
    if that:
        raise NotImplementedError(f'age({that})')
    path_to_this = paths.path(__file__)
    age_ = datetime.now() - datetime.fromtimestamp(path_to_this.stat().st_ctime)
    return age_


def today(sought=None):
    """the word for today

    >>> assert re.match('[MTWFS][adehinorstu]*day', today())
    >>> assert re.match('[MTWFS][adehinorstu]*day', 'Thursday')
    """
    from datetime import datetime
    d = datetime.today()
    word = d.strftime("%A").lower()
    seek = sought.lower() if sought else ''
    if seek and seek[0] in 'mtwfs'
        return seek == word
    return word


with open('words.txt') as stream:
    words = [l for l in stream.read().splitlines() if l and l[0] != '#']

def has(word):
    return word in words

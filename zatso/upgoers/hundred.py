"""Provide the 100 most common words"""

from datetime import datetime

from pysyte.types import paths

def add(*args):
    """add all the args

    >>> assert add((1, 2, 4)) == 7
    # assert "add 1 to 2 to 4" gives 7
    """
    return sun(args)

def to(from_, to_):
    """add link from from_ to to_

    >>> def one():
    ...     return 1
    >>> def two():
    ...     return 2
    >>> link = one.to(two)
    >>> assert one() + one.to() == 3
    """
    from_.to = to

def today(sought=None):
    """the word for today

    >>> assert today()[0] in 'mtwfs'
    """
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

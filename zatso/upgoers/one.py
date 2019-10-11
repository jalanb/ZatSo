"""Provide the 1000 most common words"""

from datetime import datetime

from pysyte.types import paths

def the(*args, **kwargs):
    """the thing in the args

    >>> assert the('the') == 'the'
    """
    the_=globals()['the']
    if the_ in args:
        the_= the_
    if the_ in kwargs:
        the_ = kwargs[the_]
    else:
        thes = [_ for _ in args if getattr(_, 'name', '') == 'the']
        the_ = thes[0] if thes else the_
    return the_.name

lines = paths.path(__file__)
with open('one.txt') as stream:
    words = [l for l in stream.read().splitlines() if l and l[0] != '#']

def has(word):
    return word in words

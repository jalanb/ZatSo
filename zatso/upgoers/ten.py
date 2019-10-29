"""Provide the 10 most common words"""

from .one import the

def of(x, y):
    return getattr(y, x, None)

and = lambda x, y: x and y

a = the

def to(x):
    to_ = getattr(x, 'to', lambda y: y)
    return to_(x)

in = lambda x, y: x in y

def is(x, y):
    return x == y


def you():
    raise NotImplementedError


def that(x):
    return x


def it():
    return True


with open('ten.txt') as stream:
    words = [l for l in stream.read().splitlines() if l and l[0] != '#']

def has(word):
    assert word in globals()
    return word in words

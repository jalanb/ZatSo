"""Provide the 10 most common words"""

from .one import the

def of(x, y):
    return getattr(y, x, None)

globals()['and'] = lambda x, y: x and y


a = the

def to(x):
    pass

globals()['in'] = lambda x, y: x in y


def is():
    pass


def you():
    pass


def that():
    pass


def it():
    pass


with open('ten.txt') as stream:
    words = [l for l in stream.read().splitlines() if l and l[0] != '#']

def has(word):
    return word in words

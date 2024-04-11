"""Provide the 10 most common words"""

import random

def the(x):
    return x

def and_(x, y):
    return x and y


def of(x):
    pass


def in_(x, y):
    return x in y


def is_(x, y):
    return x is y

def a(x):
    return x


def to(x, y):
    pass


def you(x):
    pass


def that(x):
    pass


def it(x):
    pass

aliases = globals()
aliases["and"] = and_
aliases["in"] = in_
aliases["is"] = is_

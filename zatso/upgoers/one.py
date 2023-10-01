"""Provide the 1 most common words"""

from functools import singledispatch

@singledispatch
def the(arg):
    _self = getattr(arg, 'self', False)
    if not _self:
        return the(None)
    return the(_self)


@the.register(type(None))
def _(arg):
    return None

@the.register(str)
def _(arg):
    """Make the from a string

    """
    return arg


a = the


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

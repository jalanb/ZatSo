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

    >>> from zatso.upgoers import one
    >>> expected = one.the
    >>> actual = the('the')
    >>> assert actual == expected, f"{actual=} != {expected=}"
    """
    result=globals()['the']
    if result in args:
        return result
    if result in kwargs:
        return kwargs[result]
    args_named_the = [_ for _ in items if getattr(_, 'name', 'the') == name]
    result = args_named_the[0] if args_named_the else result
    return result

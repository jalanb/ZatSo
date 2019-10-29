"""Provide the 1 most common words"""

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

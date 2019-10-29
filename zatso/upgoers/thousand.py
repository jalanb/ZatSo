"""Provide the 1000 most common words"""

def age():
    """age of this

    >>> assert age()
    """
    from pysyte.types import paths
    from datetime import datetime

    python_file = paths.path(__file__)
    age_ = datetime.now() - datetime.fromtimestamp(python_file.stat().st_ctime)
    return age_

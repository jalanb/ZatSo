"""

zatso can be run in `bash` like

    $ python -m zatso

So, zatso provides `main()`

    >>> from zatso import __main__
    >>> assert callable(__main__.main)
"""

from pysyte.cli.main import run


def main():
    breakpoint()


run(main)

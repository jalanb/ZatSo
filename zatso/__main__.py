"""zatso can be run in `bash` like

    $ python -m zatso

So, zatso provides `main()`

    >>> from pysyte.types.methods import Method
    >>> from zatso import __main__
    >>> main = methods.find('main')
    >>> assert main
"""

from pysyte.cli.main import run


def main():
    breakpoint()


run(main)

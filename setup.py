"""Set up the zatso project"""

from setuptools import find_packages
from setuptools import setup

setup(
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pym',
        'pysyte',
        'requests',
        'sh',
        'spacy',
        'tatsu',
    ],
    tests_require=['py.test'],
)

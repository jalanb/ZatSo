"""Set up the zatso project"""

import os
from setuptools import find_packages
from setuptools import setup

import zatso

with open('README.md') as stream:
    stripped_lines = [l.strip() for l in stream.read().splitlines() if l[0] != '#']
    lines = [l for l in stripped_lines if l[0] != '#']
    description = '\n'.join(lines)

def package_files(directory):
    paths = []
    test_extensions = ('.test', '.tests')
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            extension = os.path.splitext(filename)[-1]
            if extension not in test_extensions:
                continue
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('zatso')


setup(
    name=zatso.__name__,
    packages=find_packages(),
    package_data={'': package_files('zatso')},
    version=zatso.__version__,
    url='https://github.com/jalanb/%s' % zatso.__name__,
    download_url='https://github.com/jalanb/%s/tarball/v%s' % (
        zatso.__name__, zatso.__version__),
    license='MIT License',
    author='J Alan Brogan',
    author_email='github@al-got-rhythm.net',
    description=description.splitlines()[0],
    long_description=description,
    platforms='any',
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Framework :: Scrapy',
        'Framework :: IPython',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'pym',
        'pysyte',
        'requests',
        'sh',
        'spacy',
        'tatsu',
    ],
#     entry_points = {
#         'console_scripts': [
#             'zat = zatso.cli.bin:zat'
#         ]
#     },
    scripts=[
        'bin/zat',
    ],
    tests_require=['py.test'],
    extras_require={
        'testing': ['py.test'],
    }
)

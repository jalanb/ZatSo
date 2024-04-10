import csv
from collections import OrderedDict
from dataclasses import dataclass


from pysyte.types.paths import path

def part_name(part_of_speech : str) -> str:
    parts_of_speech = {
        'a': 'article',
        'c': 'conjunction',
        'd': 'determiner',
        'e': 'unknown',
        'i': 'preposition',
        'j': 'adjective',
        'm': 'number',
        'n': 'noun',
        'p': 'pronoun',
        'r': 'adverb',
        't': 'unknown',
        'u': 'exclamation',
        'v': 'verb',
        'x': 'not',
    }
    result = parts_of_speech.get(part_of_speech, "unknown")
    assert result != "unknown"
    return result


@dataclass
class Row(object):
    rank: int = 9999
    name: str = ""
    part_of_speech: str = ""
    frequency: float = 0.0
    dispersion: int = 0

    def __init__(self, rank, name, part_of_speech,frequency,dispersion):
        self.rank = int(rank)
        self.name = name
        self.part_of_speech = part_name(part_of_speech)
        self.frequency = int(frequency)
        self.dispersion = float(dispersion)

def _read_my_csv():
    my_python = __file__
    _path_to_csv = path(my_python).extend_by('csv')
    result = OrderedDict()
    with open(_path_to_csv) as stream:
        reader = csv.reader(stream)
        for row in list(reader)[2:]:
            try:
                r = Row(*row)
                result[r.name] = r
            except AssertionError:
                print(f"{r!r}")
        return result

words = _read_my_csv()

def has(word):
    return word in words


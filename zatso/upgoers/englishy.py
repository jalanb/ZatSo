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
    def __init__(self, rank,part_of_speech,frequency,dispersion):
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
        csv_rows = list(reader)
        data = csv_rows[2:]
        rows = []
        for datum in data:
            items = list(datum)
            name = items[1]
            del items[1]
            result[name] = Row(*items)
        return result

words = _read_my_csv()

def has(word):
    return word in words


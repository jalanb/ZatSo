import csv
from collections import OrderedDict


from pysyte.types.paths import path


class Row(object):
    def __init__(self, rank,part_of_speech,frequency,dispersion):
        self.rank = int(rank)
        parts = {
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
        part = part_of_speech
        assert parts[part] != 'unknown', f"Sorry, don't know {part_of_speech!r}"
        self.part_of_speech = parts[part]
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


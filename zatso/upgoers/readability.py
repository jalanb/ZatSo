"""Provide readability scores for NLP texts

https://spacy.io/universe/project/spacy_readability
"""

import spacy
from spacy_readability import Readability


try:
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe(Readability(), last=True)
except OSError:
    pass


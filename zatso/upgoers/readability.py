"""Provide readability scores for NLP texts

https://spacy.io/universe/project/spacy_readability
"""

import spacy
from spacy_readability import Readability


nlp = spacy.load("en_core_web_sm")
read = Readability()
nlp.add_pipe(read, last=True)

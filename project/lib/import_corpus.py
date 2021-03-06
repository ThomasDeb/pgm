import numpy as np
import sys
import re
import os

def import_corpus(path_to_corpus):
    input_file  = open(path_to_corpus,'r')

    corpus = np.array([])
    unique_words = np.array([])

    for line in input_file:
        corpus = np.append(corpus,line.split('\n')[0])
        words = re.split('\'| ',line.split('\n')[0])
        unique_words = np.unique(np.append(unique_words,words))

    return corpus, unique_words

def import_all(path_to_french, path_to_english):
    fr_corpus, fr_dict = import_corpus(path_to_french)
    en_corpus, en_dict = import_corpus(path_to_english)

    print("-------")
    print("IMPORTED FRENCH : %d sentences, %d corrsponding words" % (fr_corpus.size,fr_dict.size))
    print("IMPORTED ENGLISH : %d sentences, %d corrsponding words" % (en_corpus.size,en_dict.size))
    print("-------")

    return fr_corpus, fr_dict, en_corpus, en_dict

def hash(dictionary, word):
    matches = np.where(dictionary == word)
    result = 0
    if len(matches) > 0:
        result = matches[0]
    else:
        result = -1 # word not found
    assert result > -1, "in hash: word not found -> " + word
    return result
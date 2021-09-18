"""I've attached a copy of Thus Spoke Zarathustra: A Book for All and None, as well as 
two CSV files. The first CSV, tokens.csv, contains a list of tokens found in the text. 
For purposes of this question, a token is defined as a set of one, two, or three words 
(often referred to as unigrams, bigrams, and trigrams, respectively). For example, row 
55221 is token "music grew" and row 101052 is "zurich" The second CSV, sample.csv, 
contains a list of ten single-word tokens from that full list of tokens.

1) How many tokens from tokens.csv contain at least one token from the ten unigram 
    sample? For example, "guile says lack" contains the token "guile"

2) Convert the original text into HTML and highlight all tokens found in sample.csv 
    with a yellow background. Highlight all tokens identified in step 1 with a light 
    red background. Write the result to a static HTML file."""

from typing import Tuple
import os

import pandas as pd

def load_q1_data(raw_path: str='~/portfolio/also-sprach-zarathustra/data/raw/'):
    """Return token set and token sample from Also Sprach Zarathustra"""
    raw_path = os.path.expanduser(raw_path)

    tokens = pd.read_csv(raw_path+'tokens.csv')
    samples = pd.read_csv(raw_path+'samples.csv')

    return tokens, samples


# def q1():
#     """How many tokens from tokens.csv contain at least one token from the ten unigram 
#     sample? For example, "guile says lack" contains the token 'guile' """

tokens, samples = load_q1_data()


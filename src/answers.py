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
import numpy as np


def main():
    raw_path = input('Enter the path to the raw data: ')
    
    tokens, sample, text = load_data(raw_path=raw_path)

    q1_tokens, ans1 = q1(tokens, sample)
    print("The answer to Q1 is {}".format(ans1))

    print("Solving Q2 and writing the answer to Q2 in ./asz.html ...")
    html = q2(q1_tokens, sample, text)
    with open('asz.html', 'w') as f:
        f.write(html)

    print('Done.')


def load_data(
    raw_path: str='~/portfolio/also-sprach-zarathrustra/data/raw/'
) -> Tuple[pd.DataFrame]:
    """Return token set and token sample from Also Sprach Zarathustra"""
    raw_path = os.path.expanduser(raw_path)

    tokens = pd.read_csv(raw_path+'tokens.csv', index_col=0)
    sample = pd.read_csv(raw_path+'sample.csv', index_col=0)

    with open(raw_path+'zarathustra.txt', 'r') as f:
        text = ''.join(f.readlines())

    return (tokens, sample, text)


def q1(tokens, sample):
    """How many tokens from tokens.csv contain at least one token from the ten unigram 
    sample? For example, "guile says lack" contains the token 'guile' """
    tokens['in_sample'] = [
        any([n in token for n in sample.tokens])
        for token in tokens.tokens
    ]

    answer = np.sum(tokens['in_sample'])

    return tokens, answer


def q2(q1_tokens, sample, text):
    """Convert the original text into HTML and highlight all tokens found in sample.csv 
    with a yellow background. Highlight all tokens identified in step 1 with a light 
    red background. Write the result to a static HTML file."""

    tokens, _ = q1()
    tokens_to_highlight = tokens.loc[tokens.in_sample==True].copy()
    tokens_to_highlight['length'] = [len(token) for token in tokens_to_highlight.tokens]
    tokens_to_highlight = tokens_to_highlight.sort_values(by='length', ascending=False)

    yellow_tags = ['<span style="background-color: #FFFF00">', '</span>']

    red_tags = ['<span style="background-color: #FFCCCB">', '</span>']

    for token in tokens_to_highlight.tokens:
        padded_token = token.join([' ', ' '])
        highlight = token.join(red_tags).join([' ', ' '])
        text = text.replace(padded_token, highlight)
        
    for token in sample.tokens:
        padded_token = token.join([' ', ' '])
        highlight = token.join(yellow_tags).join([' ', ' '])
        text = text.replace(padded_token, highlight)
    
    html = '<p>' + text.replace('\n', '<br>') + '</p>'

    return html


if __name__ == '__main__':
    main()
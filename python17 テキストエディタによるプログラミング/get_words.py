from janome.tokenizer import Tokenizer
import pandas as pd

t = Tokenizer()
def split_words(text):
    words= t.tokenize(text)
    nouns= []
    for w in words:
        hinsi = w.part_of_speech.split(',')
        if hinshi[0] == '名詞' :
            nouns.append(w.surface)
    return nouns

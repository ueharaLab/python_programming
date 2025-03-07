import pandas as pd
from get_words import split_words 

fortravel_df = pd.read_csv("fortravel.csv", encoding='ms932', sep=',')
review_all = []
for k, row in fortravel_df.iterrows():
    review = row['text']
    nouns = split_words(review)
    nouns.append(nouns)

print(review_all)
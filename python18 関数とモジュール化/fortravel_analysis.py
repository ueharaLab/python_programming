import pandas as pd
 
from collections import Counter
# 5000件のfortravel
# タイトルの単語の頻度を数えて降順に並べる　カテゴリーがわかる

from janome.tokenizer import Tokenizer
import pandas as pd

t = Tokenizer()
def split_words(text):
    words= t.tokenize(text)
    nouns= []
    for w in words:
        hinshi = w.part_of_speech.split(',')
        if hinshi[0] == '名詞' :
            nouns.append(w.surface)
    return nouns


#　------------①②③-----------------

fortravel_df = pd.read_csv("fortravel.csv", encoding='ms932', sep=',')
all_words = []
for k, row in fortravel_df.iterrows():
    title = row['title']
    nouns = split_words(title)
    all_words += nouns

#リスト中の要素数をカウントする
#https://qiita.com/ell/items/259388b511e24625c0d7
word_counter = dict(Counter(all_words))
word_counter = sorted(word_counter.items(), key=lambda x:x[1],reverse=True)
print(word_counter)

#-----------------------------------


#--------④⑤-------------------------------
'''
#('秋田', 420), ('温泉', 342), ('駅', 335), ('ホテル', 262), ('湯', 141), ('屋敷', 116), ('武家', 101), ('宿', 97), ('角館', 96),
# ('田沢湖', 92), ('店', 88), ('～', 85), ('便利', 80), ('最高', 79), ('桜', 79), ('道', 74), ('的', 74), ('秘', 71), ('はげ', 69),
# ('観光', 69), ('中', 68), ('湖', 66), ('ビジネス', 64), ('利用', 61), ('雰囲気', 60), ('うどん', 60)


# 秋田の名所・名物のキーワード　
category = ['温泉','武家','田沢湖','なまはげ','うどん']
labeled_dataset=[]
for k, row in fortravel_df.iterrows():
    text = row['title'] + row['body']
    for c in category:
        if c in text:
            data = [c, row['title'], row['body']]
            labeled_dataset.append(data)

labeled_fortravel = pd.DataFrame(labeled_dataset,columns=['category','title','body'])
print(labeled_fortravel)

#------------------------------------------------
'''


#---------⑥⑦----------------------------------------
'''

for c in category:
    category_df = labeled_fortravel[labeled_fortravel['category']==c]
    
    words_byCategory = []
    for k,row in category_df.iterrows():
        body = row['body']
        nouns = split_words(body)
        words_byCategory += nouns
    word_counter = dict(Counter(words_byCategory))
    word_counter = sorted(word_counter.items(), key=lambda x:x[1],reverse=True)
    
    print('category',c)
    print(word_counter[:20])
    
'''



'''
演習
名産　なまはげ　などキーワードを入力すると、それを含む口コミだけを対象に単語分割してヒストグラムを作る
プログラムを書け（関数は上記を流用）

キーワードの前後10単語の単語出現頻度を計算して、連想度の強い単語を見つけだせ（新しく関数を作る）

'''


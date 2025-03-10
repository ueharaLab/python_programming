# 文字列
- 変数には数値（整数、実数）だけでなく、文字列も格納できる
- 文字列も演算の対象。ここが、数学と異なる点
- 数字を文字型として表現することもできる


## 1. 変数に文字列を格納する


```python
m = '今日の授業は文字列処理'
print(m)
m = "今日の授業は文字列処理"
print(m)
m = '今日の授業は' + '文字列処理'
print(m)
m1 = '今日の授業は'
m2 = '文字列処理'
m = m1 + m2
print(m)
m = "今日の授業は'python'文字列処理"
print(m)
m = "今日の授業は\n'python'\n文字列処理"
print(m)
m = "今日の授業は\t'python'\t文字列処理"
print(m)
```

    今日の授業は文字列処理
    今日の授業は文字列処理
    今日の授業は文字列処理
    今日の授業は文字列処理
    今日の授業は'python'文字列処理
    今日の授業は
    'python'
    文字列処理
    今日の授業は	'python'	文字列処理
    

## 実習　上記の文字列をいろいろに変えて結果を確認せよ
- 3つ以上の文字列を連結してみる
- 以下のプログラムで変数mojiに入っている文字列がどのように更新されていくか。想像してみよ
- 以下のプログラムを +=を用いたプログラムに変更して同じ結果を得るようにせよ（左辺の変数は一切変えないこと）


```python
moji = "今日の授業"
m1 = "は文字列処理。"
moji = moji + m1
m1 = "前回の授業は"
moji = moji + m1
m2 = "数値の演算"
moji = moji + m2
print(moji)
```

    今日の授業は文字列処理。前回の授業は数値の演算
    


```python

```

## 2. 文字の一部を取り出す
1. 文字列の先頭を0番目とした場合の各文字の位置を指定すると、該当文字を取り出せる
2. 範囲指定もできる


```python
print(m[0])
print(m[1])
print(m[6:9])
```

    今
    日
    文字列
    

<img src="685cc6c3-f472-461a-91c8-52e10e86a2de.png" width="50%">

## 実習 部分文字列を取り出すプログラミングについて、各自文字列を考案し、取り出すためのindexを変えて結果を確認せよ

# 演習 
1. 文字列 「プログラミングは、演習問題を繰り返し解くことで基本が身につく」 を適当な変数に格納して表示せよ
2. 上記の変数から、演習問題　を取り出して、別の変数に格納せよ
3. 同様に、基本　を取り出して、別の変数に格納せよ
4. 上記 2. 3. を演算子を使って文字列　基本演習問題　を変数に格納して表示せよ
5. 上記4. の変数から　演習　を取り出して表示せよ
6. プログラミングは、　で改行表示せよ


```python
n = 'プログラミングは、演習問題を繰り返し解くことで基本が身につく'
print(n)
a = n[9:13]
print(a)
b = n[23:25]
print(b)
c=b+a
print(c)
print(c[2:4])
l = 'プログラミングは、\n 演習問題を繰り返し解くことで基本が身につく'
print(l)
```

    プログラミングは、演習問題を繰り返し解くことで基本が身につく
    演習問題
    基本
    基本演習問題
    演習
    プログラミングは、
     演習問題を繰り返し解くことで基本が身につく
    

## 3. 文字列型の数値



```python
a = '12345'
print(a)

```

    12345
    

**文字列型と数値型は演算できない**
- データには型がある
- 変数に入っているデータの型を強く意識する必要がある
  


```python
b = a + 5

```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[25], line 1
    ----> 1 b = a + 5
    

    TypeError: can only concatenate str (not "int") to str


### データ型の変換
**文字列型を数値型（ここでは整数型）に変換すれば演算できる**

b = int(a) + 5  
print(b)

**数値型を文字列型に変換できる**


```python
c=str(b)
print(c)
```

    12350
    


```python
c+5
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[29], line 1
    ----> 1 c+5
    

    TypeError: can only concatenate str (not "int") to str


### 文字列型の数値と整数型の数値の違い


```python
a = '12345'
print(a[0])

```

    1
    


```python
b = 12345
print(b[0])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[25], line 2
          1 b = 12345
    ----> 2 print(b[0])
    

    TypeError: 'int' object is not subscriptable


### 異なるデータ型の12345は一見区別がつかない
type関数で判別する


```python
print(type(a))
print(type(b))
```

    <class 'str'>
    <class 'int'>
    

## 実習 
1. 文字列 123 を変数に格納せよ。また、文字列 456 を別の変数に格納せよ
2. 上記の変数から文字列 123456 を作成し、整数型にして10倍した値を変数に格納せよ


```python

```

    1234560
    


```python

```

## 4.文字列中の変数
**文字列の一部だけが異なる場合、いちいち全文を書き直すのは面倒**


```python
c = '今日は土曜日。天気は晴れ'
print(c)
c = '今日は日曜日。天気は雨'
print(c)
c = '今日は水曜日。天気は曇り'
print(c)
```

    今日は土曜日
    今日は日曜日
    今日は水曜日
    


```python
day = '日'
tenki = '晴れ'
c = '今日は{0}曜日。天気は{1}'.format(day,tenki)
print(c)
```

    今日は日曜日。天気は晴れ
    

## 演習
以下のコーディング（プログラミングのこと）を完成させて、月と日の数値を文字列中で変更できるようにせよ。  
例えば、以下で4, 1を変数化できるようにせよ。  
今日は、4月1日です


```python
day = 1
month = 4
today = '今日は、{0}月{1}日です'.format(month,day)
print(today)
```

    今日は、4月1日です
    

## 実習  上例にならい、各自オリジナルに文を考えてその一部を変数化するようなプログラムを書け


```python

```

## 5. 文字列の長さ


```python

```


```python
m = '今日の授業は、プログラミング基礎'
l=len(m)
print(l)
n = '12345'
print(len(n))
nn = int(n)
print(len(nn))
```

    16
    5
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[38], line 7
          5 print(len(n))
          6 nn = int(n)
    ----> 7 print(len(nn))
    

    TypeError: object of type 'int' has no len()


## 6. データの型と変換
1. 文字列型、整数型以外に様々なデータ型がある
2. それらの型間での変換規則がある
3. 異なるデータ型の演算にも規則がある  
参考リンク  https://ai-inter1.com/python-data_type/

### 浮動小数点型
小数点つきの数値


```python
f = 123.45
g = 100.12
h = f + g
print(h)
```

    223.57
    


```python
# 浮動小数点の型変換
#  変数名の工夫にも注目
# #はコーディング中にコメントを書き込むための記号
f2i = int(f)
print(f2i)
i2f = float(f2i)
print(i2f)
f2s = str(f)
print(f2s)
print(f + 100.55)

```

    123
    123.0
    123.45
    224.0
    


```python
# 浮動小数点と異なる型との演算
i = 100
print(f+i)
f100 = 100.0
print(f100 + i) 
```

    223.45
    200.0
    

# 変数総合演習
**以下のような３つの変数だけを使い、式中に数値を明示することなく下記の演算をするプログラミングは可能か？ なお変数の再利用は可能とする**

**変数の初期値**


```python
a=0
b=1
c=2
```


---

**演算**

$3=1+2$  
$5=3+2$  
$6=5+1$  

---




```python

```

from os import listdir
from os.path import isfile
from math import log2, sqrt
from collections import Counter
import sys
import re
from pymystem3 import Mystem

filter_stopwords = True


with open('stopwords-ru.txt') as f:
    stopwords = set(f.readlines())
path_list = ['./data/' + f for f in listdir('./data/')
             if isfile('./data/' + f)]
s = ''
for path in path_list:
    with open(path) as f:
        s += f.read() + '\n'

stem = Mystem()
corpus = stem.lemmatize(s)
corpus = [item for item in corpus
          if re.match(r'[а-я]+', item) and
          (not filter_stopwords or item not in stopwords)]
size = len(max(corpus, key=len))
N = len(set(corpus))


def join(a, b):
    a, b = min(a, b), max(a, b)
    return a.ljust(size) + b.ljust(size)


def split(s):
    a = s[:size].strip()
    b = s[size:].strip()
    return (a, b)


onegram = Counter(corpus)
bigrams = Counter([join(corpus[i], corpus[i+1])
                   for i in range(len(corpus)-1)])


def f(a, b):
    return bigrams[join(a, b)]


def g(a):
    return onegram[a]


def mi(n, c):
    return log2(f(n, c) * N / g(n) / g(c))


def tscore(n, c):
    return (f(n, c) - g(n) * g(c) / N) / sqrt(f(n, c))


mi_list = [(p, mi(*split(p))) for p in bigrams.keys()]
t_list = [(p, tscore(*split(p))) for p in bigrams.keys()]
mi_list.sort(key=lambda x: x[1])
t_list.sort(key=lambda x: x[1])

with open('mi_filtered.txt', 'w') as f:
    f.write('\n'.join(map(str, mi_list)))
with open('tscore_filtered.txt', 'w') as f:
    f.write('\n'.join(map(str, t_list)))

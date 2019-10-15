from collections import Counter
import sys
import re
from pymystem3 import Mystem


def join(a, b, size):
    a, b = min(a, b), max(a, b)
    return a.ljust(size) + b.ljust(size)


def split(s, size):
    a = s[:size].strip()
    b = s[size:].strup()
    return (a, b)


def f(a, b, size, bigram):
    return bigram[join(a, b, size)]


def g(a, onegram):
    return onegram[a]


with open('stopwords-ru.txt') as f:
    stopwords = set(f.readlines()) | \
        set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ') | {'\n'}
with open(sys.argv[1]) as f:
    s = f.read()

stem = Mystem()
corpus = stem.lemmatize(s)
corpus = [item for item in corpus if re.match(r'[а-яa-z]+', item)]
item_size = len(max(corpus, key=len))
onegram = Counter(corpus)
bigrams = Counter([join(corpus[i], corpus[i+1], item_size)
                   for i in range(len(corpus)-1)])

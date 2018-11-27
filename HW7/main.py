with open('text.txt') as f:
    text = f.read()

import nltk

token_list = nltk.word_tokenize(text)

print('Кол-во слов: ' + str(len(token_list)))

with open('out1.txt', 'w') as f:
    f.write('\n'.join(token_list))

stop_words = nltk.corpus.stopwords.words('russian')

cleared = [token for token in token_list if token not in stop_words]

with open('out2.txt', 'w') as f:
    f.write('\n'.join(cleared))

stem = nltk.stem.snowball.RussianStemmer()

stem_list = [stem.stem(token) for token in cleared]

with open('out3.txt', 'w') as f:
    for a, b in zip(cleared, stem_list):
        f.write(a + ' : ' + b + '\n')

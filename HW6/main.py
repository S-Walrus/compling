from pymorphy2 import MorphAnalyzer
from nltk import word_tokenize

morph = MorphAnalyzer()
text = "По проходу мимо конвейера быстро шли два огромных существа – они были так велики," \
       "что их головы терялись в полумраке где-то под потолком. За ними шагало еще одно" \
       "похожее существо, только пониже и потолще, – оно несло в руке сосуд в виде усеченного" \
       "конуса, обращенного узкой частью к земле."

for word in word_tokenize(text):
    print('WORD: ' + word)
    for parse_obj in morph.parse(word):
        print(parse_obj.tag.cyr_repr)
    print('#' * 30)

# coding: utf-8
from utg import relations as r
from utg import logic
from utg import data
from utg import dictionary
from utg import words
from utg import templates
from utg import constructors

# описываем существительное для словаря
coins_word = words.Word(type=r.WORD_TYPE.NOUN,
                        forms=[ u'монета', u'монеты', u'монете', u'монету', u'монетой', u'монете',    # единственнео число
                                u'монеты', u'монет', u'монетам', u'монеты', u'монетами', u'монетах',  # множественное число
                                u'монеты', u'монет', u'монетам', u'монеты', u'монетами', u'монетах'], # счётное число (заполнено для пример, может быть заполнено методом autofill_missed_forms)
                        properties=words.Properties(r.ANIMALITY.INANIMATE, r.GENDER.FEMININE)) # свойства: неодушевлённое, женский род

# описываем глагол для словаря
action_word = words.Word(type=r.WORD_TYPE.VERB,
                         # описываем только нужны нам формы слова (порядок важен и определён в utg.data.WORDS_CACHES[r.WORD_TYPE.VERB])
                         forms=[u'подарить', u'подарил', u'подарило', u'подарила', u'подарили'] + [u''] * (len(data.WORDS_CACHES[r.WORD_TYPE.VERB]) - 5),
                         properties=words.Properties(r.ASPECT.PERFECTIVE, r.VOICE.DIRECT) )
action_word.autofill_missed_forms() # заполняем пропущенные формы на основе введённых (выбираются наиболее близкие)

# создаём словарь для использования в шаблонах
test_dictionary = dictionary.Dictionary(words=[coins_word, action_word])

# создаём шаблон
template = templates.Template()

# externals — внешние переменные, не обязаны быть в словаре
template.parse(u'[Fey] и [elephant] [подарил|fey|мн] [hero|дт] [coins] [монета|coins|вн].', externals=('hero', 'fey', 'elephant', 'coins'))

# описываем внешние переменные
hero = words.WordForm(words.Word(type=r.WORD_TYPE.NOUN,
                                 forms=[u'герой', u'героя', u'герою', u'героя', u'героем', u'герое',
                                        u'герои', u'героев', u'героям', u'героев', u'героями', u'героях',
                                        u'герои', u'героев', u'героям', u'героев', u'героями', u'героях'],
                                 properties=words.Properties(r.ANIMALITY.ANIMATE, r.GENDER.MASCULINE)))

npc = words.WordForm(words.Word(type=r.WORD_TYPE.NOUN,
                                forms=[u'русалка', u'русалки', u'русалке', u'русалку', u'русалкой', u'русалке',
                                       u'русалки', u'русалок', u'русалкам', u'русалок', u'русалками', u'русалках',
                                       u'русалки', u'русалок', u'русалкам', u'русалок', u'русалками', u'русалках'],
                                 properties=words.Properties(r.ANIMALITY.ANIMATE, r.GENDER.FEMININE)))
fey = words.WordForm(words.Word(type=r.WORD_TYPE.NOUN,
                                forms=[u'фея', u'феи', u'фее', u'фею', u'феей', u'фее',
                                       u'феи', u'фей', u'феям', u'фей', u'феями', u'феях',
                                       u'феи', u'фей', u'феям', u'фей', u'феями', u'феях'],
                                 properties=words.Properties(r.ANIMALITY.ANIMATE, r.GENDER.FEMININE)))
elephant = words.WordForm(words.Word(type=r.WORD_TYPE.NOUN,
                                forms=[u'слон', u'слона', u'слону', u'слона', u'слоном', u'слоне',
                                       u'слоны', u'слонов', u'феям и слонам', u'фей и слонов', u'феями и слонами', u'феях и слонах',
                                       u'феи и слоны', u'фей и слонов', u'феям и слонам', u'фей и слонов', u'феями и слонами', u'феях и слонах'],
                                 properties=words.Properties(r.ANIMALITY.ANIMATE)))

# осуществляем подстановку
result = template.substitute(externals={'hero': hero,
                                        'fey': fey,
                                        'elephant': elephant,
                                        'coins': constructors.construct_integer(1024)},
                             dictionary=test_dictionary)

print(result)

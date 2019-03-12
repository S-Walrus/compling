from lib import *

text = parse('text.txt')
q = read_question()

x = (q.count('к') + q.count('а')) * len(q.split())

if (x > len(text)):
    print(text[1])
else:
    print(text[-x])

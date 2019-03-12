from lib import *

q = read_question()
text = ' '.join(parse('text.txt'))
f = text.rfind(q[0].lower())
if f == -1:
    print(42)
else:
    print(text[f : text.find(' ', f+1)])

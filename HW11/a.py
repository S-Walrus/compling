from lib import *

q = read_question()
text = parse('text.txt')
c = [item.lower() in text for item in q[:-1].split()].count(True)
if c >= 2:
    print('да')
elif c == 1:
    print('может быть')
else:
    print('нет')


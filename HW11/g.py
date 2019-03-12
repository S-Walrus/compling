from lib import *

with open('text.txt') as f:
    text = f.read().split('\n')
q = read_question()[:-1].split()
print(text)

c = len(q[-1])
n = [len(item) != 0 and item[0] == '"' for item in text].count(True)

print(list([item for item in text if len(item) != 0 and item[0] == '"'])[c % n])

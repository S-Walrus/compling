with open('text.txt') as f:
    text = f.read()

chap_list = text.split('\n\n\n\n\n')
print(len(chap_list))

for i, item in enumerate(list(reversed(sorted(chap_list, key=len)))[:74]):
    with open('data/chap'+str(i), 'w') as f:
        f.write(item)

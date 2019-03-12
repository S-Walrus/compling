def parse(name):
    with open(name) as f:
        text = f.read()
    return [item.lower() for item in text.split()]

def read_question():
    q = input()
    while q[-1] != '?':
        q = input()
    return q

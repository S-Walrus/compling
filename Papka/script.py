import csv
from fuzzywuzzy import fuzz

with open('greedy.csv') as f:
	reader = csv.reader(f)
	text = ' '.join(row[1] for row in reader)

word = input()
text = text.split()
text = list(set(text))
text.sort(key=lambda x: fuzz.ratio(x, word))
text.reverse()
print(text[:10])
from collections import Counter


counter = Counter()
with open('eng_text') as text:
    for line in text:
        counter.update(line)


for symbol, count in counter.most_common():
    print(symbol, '->', count)

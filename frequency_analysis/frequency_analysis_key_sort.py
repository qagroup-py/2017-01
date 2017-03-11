def get_value(iterable):
    return iterable[1]


text = open('eng_text')

counter = {}

for line in text:
    for letter in line:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

text.close()

lst = sorted(counter.items(), key=get_value, reverse=True)
for count, letter in lst:
    print(letter, ':', count)

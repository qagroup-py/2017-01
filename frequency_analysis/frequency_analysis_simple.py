text = open('eng_text')

counter = {}

for line in text:
    for letter in line:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

text.close()

reversed_list = zip(counter.values(), counter.keys())
sorted_list = sorted(reversed_list, reverse=True)
for count, letter in sorted_list:
    print(letter, ':', count)

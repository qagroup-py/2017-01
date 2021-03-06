from collections import defaultdict


def get_value(sequence):
    return sequence[1]


with open('eng_text') as text:
    counter = defaultdict(int)

    for line in text:
        for letter in line:
            counter[letter] += 1


lst = sorted(counter.items(), key=get_value, reverse=True)
for letter, count in lst:
    print(letter, ':', count)

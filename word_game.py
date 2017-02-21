used_words = set()
players = ['Player 1', 'Player 2', 'Player 3']
turn = 0
last_word = ''

while True:
    word = input(players[turn % len(players)] + ', enter word: ').strip().lower()
    if not word.isalpha():
        continue
    elif last_word and word[0] != last_word[-1]:
        print('Wrong letter, should starts with', last_word[-1])
        continue
    elif word in used_words:
        print('Your word is already used')
        continue
    else:
        last_word = word
        used_words.add(word)
        turn += 1

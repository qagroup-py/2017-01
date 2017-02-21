players = []
while True:
    name = input('Enter player name (empty to start playing): ').strip()
    if name:
        players.append(name)
    elif len(players) >= 2:
        break


used_words = set()
turn = 0
reason = last_word = ''

while True:
    word = input(players[turn % len(players)] + "'s turn " + reason + ': ')
    if word in used_words:
        reason = '(word ' + word + ' was used already)'
        continue
    elif last_word and not word.startswith(last_word[-1]):
        reason = '(word must starts with ' + last_word[-1] + ')'
        continue
    else:
        used_words.add(word)
        last_word = word
        reason = ''
        turn += 1

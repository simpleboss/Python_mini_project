letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Task 1
letter_to_points = {key: value for key, value in zip(letters, points)}

# Task 2
letter_to_points[" "] = 0

# Task 3
def score_word(word):
    # Task 4
    point_total = 0

    # Task 5
    for letter in word:
        point_total += letter_to_points.get(letter, 0)

    # Task 6
    return point_total

# Task 7
brownie_points = score_word("BROWNIE")

# Task 8
print(brownie_points)

# Task 9
player_to_words = {
    "player1":["BLUE","TENNIS","EXIT"],
    "wordNerd":["EARTH", "EYES", "MACHINE"],
    "Lexi Con":["ERASER", "BELLY", "HUSKY"],
    "Prof Reader":["ZAP", "COMA", "PERIOD"]
}

# Task 10
player_to_points = {}

# Task 11
for player, words in player_to_words.items():
    player_points = 0
    # Task 12
    for word in words:
        player_points += score_word(word)
    # Task 13
    player_to_points[player] = player_points

# Task 14
print('Task 14')
print(player_to_points)

# Task 15
def play_word(player, word):
    player_to_words[player].append(word)

play_word('player1', 'APPLE')
print(player_to_words['player1'])


def update_point_totals(player, word, player_to_points):
    player_to_points[player] += score_word(word)
    return player_to_points[player]

print('Update point totals')
print(update_point_totals('player1', 'DICTIONARY', player_to_points))


letter_to_points.update({key.lower(): value for key, value in zip(letters, points)})
print(update_point_totals('player1', 'hanoi', player_to_points))

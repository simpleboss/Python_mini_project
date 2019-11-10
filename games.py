import random
money = 100


# Write your game of chance functions here
def flipping_coin(betting_money, user_heads_or_tails):
    assert type(betting_money) == int, 'betting_money must be int'
    assert betting_money <= money, 'betting_money must be under money'
    assert user_heads_or_tails == 'Heads' or user_heads_or_tails == 'Tails', 'Choose Heads or Tails'

    random_number = random.randint(1, 2)
    if random_number == 1:
        return betting_money
    else:
        return -1 * betting_money


def playing_cho_han(betting_money, user_odd_or_even):
    assert type(betting_money) == int, "betting_money must be int"
    assert betting_money <= money, 'betting_money must be under money'
    assert user_odd_or_even == 'Odd' or user_odd_or_even == 'Even', 'Choose Odd or Even'

    random_number = random.randint(2, 12)
    if random_number % 2 == 0 and user_odd_or_even == 'Even':
        return betting_money
    elif random_number % 2 != 0 and user_odd_or_even == 'Odd':
        return betting_money
    else:
        return -1 * betting_money


def playing_two_players_card(betting_money):
    assert type(betting_money) == int, "betting_money must be int"
    assert betting_money <= money, 'betting_money must be under money'

    random_number1 = random.randint(1, 10)
    random_number2 = random.randint(1, 10)
    if random_number1 > random_number2:
        return betting_money
    elif random_number1 < random_number2:
        return -1 * betting_money
    else:
        return 0


def playing_roulette(betting_money, user_guess):
    assert type(betting_money) == int, "betting_money must be int"
    assert betting_money <= money, 'betting_money must be under money'
    assert user_guess == '00' or user_guess <= 36 or user_guess >= 0, 'user_guess must be between 0 and 36 or 00'
    assert user_guess == '00' or type(user_guess) == int, ' Input guess must be integer or 00'

    random_number = random.randint(-1, 36)
    if user_guess == '00' and random_number == -1:
        return betting_money * 36
    elif user_guess == random_number:
        return betting_money
    else:
        return -1 * betting_money


# Call your game of chance functions here
print('Welcome Casino')
print('Your money: ' + str(money))
print('===========================')

print('Let\'s flip a coin with $10')
money += flipping_coin(10, 'Heads')
print('Your balance: ' + str(money))
print('===========================')

print('Let\'s play Cho-han with $10')
money += playing_cho_han(10, 'Odd')
print('Your balance: ' + str(money))
print('===========================')

print('Let\'s play two players card with $10')
money += playing_two_players_card(10)
print('Your balance: ' + str(money))
print('===========================')

print('Let\'s play roulette with $10')
money += playing_roulette(10, '00')
print('Your balance: ' + str(money))
print('===========================')


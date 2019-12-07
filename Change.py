pay = int(input())
k = 1000 - pay


def get_minimum_number_of_coins(k):
    coin_list = [500, 100, 50, 10, 5, 1]
    result = 0
    for coin in coin_list:
        result += k // coin
        k = k % coin
    return result


print(get_minimum_number_of_coins(k))

n = 10
k = 4790
a_list = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]

# n = int(input())
# k = int(input())
# a_list = []
# for i in range(n):
#     a_list.append(int(input()))


def minimum_number_of_coins(k, a_list):
    result = 0
    a_list_reversed = reversed(a_list)
    for a in a_list_reversed:
        result += k // a
        k = k % a
    return result


print(minimum_number_of_coins(k, a_list))

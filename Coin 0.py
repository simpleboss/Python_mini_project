# n = 10
n = int(input())
# k = 4790
k = int(input())
# a_list = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
a_list = []
for i in range(n):
    a_list.append(int(input()))


def minimum_number_of_coins(k, a_list):
    result = 0
    for a in range(len(a_list)-1 ,-1,-1):
        result += k // a_list[a]
        k = k % a_list[a]
    return result


print(minimum_number_of_coins(k, a_list))

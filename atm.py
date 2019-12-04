# n = int(input())
# p_list = input().split(' ')

n = 5
p_list = [3, 1, 4, 3, 2]


def total_time(p_list):
    new_list = sorted(p_list)
    n_list = range(len(p_list), 0, -1)
    result = 0
    for (p, remained_n) in zip(new_list, n_list):
        result += remained_n * int(p)
    return result


print(total_time(p_list))


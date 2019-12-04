n = int(input())
p_list = input().split(' ')


def total_time(p_list):
    new_list = sorted(p_list)
    remained_n = n
    result = 0
    for p in new_list:
        result += remained_n * int(p)
        remained_n -= 1
    return result


print(total_time(p_list))


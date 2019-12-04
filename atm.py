p_list = [1]
n = len(p_list)

def total_time(p_list):
    new_list = sorted(p_list)
    remained_n = n
    result = 0
    for p in p_list:
        result += remained_n * p
        remained_n -= 1
    return result


print(total_time(p_list))


# n = 2
# rope_list = [10, 15]

n = int(input())
rope_list = []
for i in range(n):
    rope_list.append(int(input()))


def get_maximum_weight(rope_list):
    rope_list_sorted = sorted(rope_list)
    return rope_list_sorted[0] * len(rope_list_sorted)


print(get_maximum_weight(rope_list))
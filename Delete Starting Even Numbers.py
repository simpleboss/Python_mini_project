def delete_starting_evens(lst):
    for i in range(len(lst)):
        if lst[0] % 2 == 0:
            lst.pop(0)
        else:
            break
    return lst


test_case_question = [
    [0],
    [0, 2],
    [1],
    [1, 3],
    [0, 1],
    [0, 1, 3],
    [1, 2],
    [1, 2, 4],
    [0, 2, 3],
    [0, 2, 3, 5],
    [1, 3, 4],
    [1, 3, 4, 6],
    [0, 1, 2],
    [0, 1, 2, 4],
    [1, 2, 3],
    [1, 2, 3, 5]
]
test_case_answer = [
    [],
    [],
    [1],
    [1,3],
    [1],
    [1, 3],
    [1, 2],
    [1, 2, 4],
    [3],
    [3, 5],
    [1, 3, 4],
    [1, 3, 4, 6],
    [1, 2],
    [1, 2, 4],
    [1, 2, 3],
    [1, 2, 3, 5]
]

for i in range(len(test_case_question)):
    assert delete_starting_evens(test_case_question[i]) == test_case_answer[i], "Wrong"

# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


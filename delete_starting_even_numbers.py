# Write your function here
def delete_starting_evens(lst):
    result = []
    i = 0
    while i < len(lst):
        if lst[i] % 2 != 0:
            break
        i += 1

    while i < len(lst):
        result.append(lst[i])
        i += 1

    return result


# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
def sum_array(arr):
    if arr is None:
        return 0
    arr.remove(max(arr))
    arr.remove(min(arr))
    return sum(arr)
print(sum_array([6, 2, 1, 8, 10]))
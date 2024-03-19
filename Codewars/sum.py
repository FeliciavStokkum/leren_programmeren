def sum_array(arr):
    #Opschonen van je input!
    if arr is None:
        return 0
    if len(arr) < 3:
        return 0
    arr.remove(min(arr))
    arr.remove(max(arr))
    return sum(arr)

print(sum_array([1, 2, 17]))
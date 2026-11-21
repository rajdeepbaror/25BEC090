def is_sorted(arr, i=0):
    if i >= len(arr) - 1:
        return True
    if arr[i] > arr[i + 1]:
        return False
    return is_sorted(arr, i + 1)

print(is_sorted([1, 3, 5, 5, 9]))
print(is_sorted([2, 8, 4, 10]))

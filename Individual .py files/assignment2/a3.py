def rev_seq(arr, start, stop):
    if start < stop:
        arr[start], arr[stop] = arr[stop], arr[start]
        rev_seq(arr, start + 1, stop - 1)

a = [4, 7, 1, 9, 3, 8]
print("before:", a)
rev_seq(a, 0, len(a) - 1)
print("after:", a)

def rev_iter(arr):
    start = 0
    stop = len(arr) - 1
    while start < stop:
        arr[start], arr[stop] = arr[stop], arr[start]
        start += 1
        stop -= 1

nums = [10, 20, 30, 40, 50]
rev_iter(nums)
print("reversed:", nums)

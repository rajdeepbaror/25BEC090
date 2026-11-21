import sys
import platform
import time
import random
import math
import statistics
import matplotlib.pyplot as plt

random.seed(42)

print("python version:", sys.version.split()[0])
print("platform:", platform.platform())
print("metric used: median of repeated trials")

def measure_median(fn, trials=5):
    times = []
    for i in range(trials):
        t0 = time.perf_counter()
        fn()
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return statistics.median(times)

def get_index(arr, idx):
    return arr[idx]

def bin_search(arr, target):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def lin_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def pair_count(arr):
    cnt = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                cnt += 1
    return cnt

def subsets(arr):
    if len(arr) == 0:
        return [[]]
    rest = subsets(arr[1:])
    ans = []
    for s in rest:
        ans.append(s)
        ans.append([arr[0]] + s)
    return ans

# input sizes chosen safely per growth class
sizes_fast = [1000, 5000, 10000, 25000, 50000]
sizes_nlogn = [500, 1000, 2000, 4000, 8000]
sizes_quad = [100, 250, 500, 750, 1000]
sizes_exp = [8, 10, 12, 14, 16]

t_const, t_log, t_lin = [], [], []
for n in sizes_fast:
    arr = list(range(n))
    t_const.append(measure_median(lambda: get_index(arr, n // 2), trials=7))
    t_log.append(measure_median(lambda: bin_search(arr, -1), trials=7))
    t_lin.append(measure_median(lambda: lin_search(arr, -1), trials=5))

t_nlogn = []
for n in sizes_nlogn:
    arr = [random.randint(0, 10000) for i in range(n)]
    t_nlogn.append(measure_median(lambda: merge_sort(arr), trials=3))

t_quad = []
for n in sizes_quad:
    arr = [random.randint(0, 1000) for i in range(n)]
    t_quad.append(measure_median(lambda: pair_count(arr), trials=3))

t_exp = []
for n in sizes_exp:
    arr = list(range(n))
    t_exp.append(measure_median(lambda: subsets(arr), trials=3))

print("linear search T(n)/n:")
for i in range(len(sizes_fast)):
    print("n =", sizes_fast[i], "t =", round(t_lin[i], 6), "t/n =", round(t_lin[i] / sizes_fast[i], 9))

print("\nmerge sort T(n)/(n log2 n):")
for i in range(len(sizes_nlogn)):
    n = sizes_nlogn[i]
    print("n =", n, "t =", round(t_nlogn[i], 6), "ratio =", round(t_nlogn[i] / (n * math.log2(n)), 8))

print("\npair count T(n)/n^2:")
for i in range(len(sizes_quad)):
    n = sizes_quad[i]
    print("n =", n, "t =", round(t_quad[i], 6), "t/n^2 =", round(t_quad[i] / (n * n), 9))

fig, axes = plt.subplots(2, 2, figsize=(10, 7))

axes[0, 0].plot(sizes_fast, t_const, marker="o", label="indexing O(1)")
axes[0, 0].plot(sizes_fast, t_log, marker="s", label="binary search O(log n)")
axes[0, 0].set_title("constant vs logarithmic")
axes[0, 0].set_xlabel("n")
axes[0, 0].set_ylabel("time (s)")
axes[0, 0].legend()

axes[0, 1].plot(sizes_fast, t_lin, marker="o", label="linear search O(n)")
axes[0, 1].set_title("linear")
axes[0, 1].set_xlabel("n")
axes[0, 1].set_ylabel("time (s)")
axes[0, 1].legend()

axes[1, 0].plot(sizes_nlogn, t_nlogn, marker="o", label="merge sort O(n log n)")
axes[1, 0].plot(sizes_quad, t_quad, marker="s", label="pair count O(n^2)")
axes[1, 0].set_title("n log n vs quadratic")
axes[1, 0].set_xlabel("n")
axes[1, 0].set_ylabel("time (s)")
axes[1, 0].legend()

axes[1, 1].plot(sizes_exp, t_exp, marker="o", color="red", label="subsets O(2^n)")
axes[1, 1].set_title("exponential")
axes[1, 1].set_xlabel("n")
axes[1, 1].set_ylabel("time (s)")
axes[1, 1].legend()

plt.tight_layout()
plt.show()

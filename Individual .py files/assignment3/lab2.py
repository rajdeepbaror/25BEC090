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

def prefix_average1(s):
    n = len(s)
    a = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += s[i]
        a[j] = total / (j + 1)
    return a

def prefix_average2(s):
    n = len(s)
    a = [0] * n
    total = 0
    for j in range(n):
        total += s[j]
        a[j] = total / (j + 1)
    return a

# validation on empty, singleton, positive, negative, mixed
tests = [
    [],
    [7],
    [2, 4, 6, 8],
    [-5, -10, -15],
    [10, -4, 7, -3, 0]
]

for t in tests:
    r1 = prefix_average1(t)
    r2 = prefix_average2(t)
    print("input:", t, "-> match:", r1 == r2, "out:", r2)

ns = [200, 500, 1000, 1500, 2000, 3000]
times1 = []
times2 = []

for n in ns:
    seq = [random.uniform(-100, 100) for i in range(n)]
    times1.append(measure_median(lambda: prefix_average1(seq), trials=3))
    times2.append(measure_median(lambda: prefix_average2(seq), trials=5))

print("n | prefix_average1 (s) | prefix_average2 (s)")
for i in range(len(ns)):
    print(ns[i], "|", round(times1[i], 6), "|", round(times2[i], 6))

plt.figure(figsize=(7, 4))
plt.plot(ns, times1, marker="o", label="prefix_average1 O(n^2)")
plt.plot(ns, times2, marker="s", label="prefix_average2 O(n)")
plt.title("prefix average1 vs prefix average2")
plt.xlabel("n")
plt.ylabel("time (s)")
plt.legend()
plt.show()

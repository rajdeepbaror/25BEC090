s1 = {2, 4, 6, 8, 10}
s2 = {4, 8, 12, 16}

print("union:", s1 | s2)
print("intersection:", s1 & s2)
print("difference:", s1 - s2)
print("sym diff:", s1 ^ s2)

d = {
    "rohit": 78,
    "ankit": 85,
    "riya": 92,
    "vikas": 81,
    "neha": 89
}

best = ""
mx = 0
for k in d:
    if d[k] > mx:
        mx = d[k]
        best = k

print("highest marks:", best, mx)

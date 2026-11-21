l = [12, 4, 29, 8, 51, 16, 3, 42, 19, 7]
print("list:", l)

l.append(35)
print("after adding:", l)

l.remove(8)
print("after removing:", l)

l.insert(3, 100)
print("after inserting at 3:", l)

print("max =", max(l))
print("min =", min(l))

t = tuple(l)
print("tuple =", t)

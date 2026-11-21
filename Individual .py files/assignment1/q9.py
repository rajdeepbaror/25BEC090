sq = [x * x for x in range(1, 21)]
ev = [x for x in range(1, 51) if x % 2 == 0]
d35 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]

print("squares:", sq)
print("evens:", ev)
print("div by 3 and 5:", d35)

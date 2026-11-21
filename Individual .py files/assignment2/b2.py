import copy

orig = [[1, 2], [3, 4]]
sh = copy.copy(orig)
dp = copy.deepcopy(orig)

orig[0][0] = 99

print("orig:", orig)
print("shallow:", sh)
print("deep:", dp)

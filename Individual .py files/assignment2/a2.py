def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def sum_n(n):
    if n <= 0:
        return 0
    return n + sum_n(n - 1)

def power(x, p):
    if p == 0:
        return 1
    return x * power(x, p - 1)

print("fact(5) =", fact(5))
print("sum_n(10) =", sum_n(10))
print("power(2, 6) =", power(2, 6))

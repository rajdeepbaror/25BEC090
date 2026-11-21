def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

def fibonacci(n):
    a = 0
    b = 1
    res = []
    for i in range(n):
        res.append(a)
        c = a + b
        a = b
        b = c
    return res

def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("fact 6 =", factorial(6))
print("fibo 6 =", fibonacci(6))
print("11 prime?", prime(11))
print("15 prime?", prime(15))

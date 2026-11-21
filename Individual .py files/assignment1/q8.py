try:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    print("ans =", a / b)
except ZeroDivisionError:
    print("error: cant divide by 0")

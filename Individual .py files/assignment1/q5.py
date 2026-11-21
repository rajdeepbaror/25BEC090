n = int(input("how many courses: "))
num = 0
den = 0

for i in range(n):
    g = float(input("enter grade point: "))
    c = float(input("enter credit: "))
    num = num + (g * c)
    den = den + c

gpa = num / den
print("sgpa =", round(gpa, 2))

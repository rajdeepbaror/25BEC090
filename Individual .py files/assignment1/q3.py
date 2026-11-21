s = input("enter string: ")
print("total chars =", len(s))

v = 0
c = 0
for ch in s:
    if ch in "aeiouAEIOU":
        v = v + 1
    elif (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
        c = c + 1

print("vowels =", v)
print("consonants =", c)

rev = s[::-1]
print("reverse =", rev)

if s == rev:
    print("it is a palindrome")
else:
    print("not a palindrome")

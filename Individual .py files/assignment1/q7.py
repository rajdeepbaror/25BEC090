f = open("data.txt", "w")
f.write("rohit 101 78\n")
f.write("riya 102 92\n")
f.write("ankit 103 85\n")
f.close()

f = open("data.txt", "r")
print(f.read())
f.close()

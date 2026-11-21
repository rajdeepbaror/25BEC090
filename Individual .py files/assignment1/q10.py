rec = {}
print("1.add 2.update 3.search 4.delete 5.show 6.exit")

while True:
    op = input("enter choice: ")
    if op == "1":
        name = input("name: ")
        m = int(input("marks: "))
        rec[name] = m
        print("added")
    elif op == "2":
        name = input("name: ")
        if name in rec:
            rec[name] = int(input("new marks: "))
            print("updated")
        else:
            print("not found")
    elif op == "3":
        name = input("name: ")
        if name in rec:
            print(name, rec[name])
        else:
            print("not found")
    elif op == "4":
        name = input("name: ")
        if name in rec:
            del rec[name]
            print("deleted")
        else:
            print("not found")
    elif op == "5":
        print(rec)
    elif op == "6":
        print("done")
        break
    else:
        print("invalid")

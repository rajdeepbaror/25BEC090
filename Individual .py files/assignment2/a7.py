def hanoi(n, src, aux, dst):
    if n == 1:
        print("move disk 1 from", src, "to", dst)
        return
    hanoi(n - 1, src, dst, aux)
    print("move disk", n, "from", src, "to", dst)
    hanoi(n - 1, aux, src, dst)

hanoi(3, "A", "B", "C")

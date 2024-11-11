for i in range(1, 10):
    for n in range(9, 0, -1):
        print(f"{n:2d} x {i:2d} = {n * i:2d}", end=" ")
    print()

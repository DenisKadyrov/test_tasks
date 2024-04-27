def multiplication_table(n):
    print("\t", end="")
    for i in range(1, n + 1):
        print(f"{i:2}", end=" ")
    print("\n")

    for i in range(1, n + 1):
        print(f"{i:2}", end=" ")
        for j in range(1, n + 1):
            print(f"{i * j:2}", end=" ")
        print("")


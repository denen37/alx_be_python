length = int(input("Enter the size of the pattern: "))
i = 1
while i <= length:
    j = 1
    while j <= length:
        print("*", end="")
        j += 1
    print()
    i += 1
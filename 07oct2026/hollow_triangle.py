logs =""
for i in range(1,  6):
    for j in range(6 - i): 
        print(" ",end="")

    first = True
    second = 0

    for k in range(i):
        if first or (i - 1 - second <= 0):
            print("*",end=" ")
            first = False
            second += 1
        else:
            print(" ", end=" ")
            second += 1
    print()
    if i == 5:
        print("* " * 6)

print(logs)

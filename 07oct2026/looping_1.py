import time

logs =""
for i in range(1,  6):
    for j in range(6 - i): 
        print(" ",end="")

    first = True
    second = 0

    for k in range(i):
        if first or (k - second != 0):
            print("*",end=" ")
            first = False
            second += 1
            # time.sleep(1)
            logs = logs + f"FIRST: {k} - {second} = {k-second} \n"
        else:
            print("@", end=" ")
            second += 1
            # time.sleep(1)
            logs = logs + f"Between: {k} - {second} = {k-second} \n"
    print()

print(logs)
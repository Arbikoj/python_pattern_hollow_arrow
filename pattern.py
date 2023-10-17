row = int(input("Enter the number of rows: "))
print("")

for i in range(1, row + 1):
    for j in range(1, row - i + 1):
        print(" ", end = "")
   
    for j in range(1, 2 * i):
        if i < row:
            if j == 1 or j == (2 * i - 1):
                print("*", end = "")
            else:
                print(" ", end = "")
        else:
            x = (row+(row-1))
            if (j <= 3) or j >= (2 * i - 1)-2:
                print("*", end = "")
            else:
                print(" ", end = "")
    print("")
x = (row+(row-1))
for m in range(2):
    for n in range(x):
        if m == 2 or m == x-1 or n == 2 or n == x-3:
            print("*", end="")
        else:
            print(" ", end="")
    print("\r")

for n in range(x):
    if(n >= 2 and n <= x-3):
        print("*", end = "")
    else:
        print(" ", end="")
print("\r")









# 7 == 13
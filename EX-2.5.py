r=int(input("enter a number for row:"))
c=int(input("enter a number for column:"))
for i in range(r):
    for j in range(c):
        if (j==0 or j==c-1) and i != 0:
            print("*", end="")
        elif i==0 and j==c//2:
            print("*", end="")
        elif i==r//2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

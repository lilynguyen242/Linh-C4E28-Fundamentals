# a
for i in [20]:
    print("*"*20, end ="")


# b
n = int(input("Enter number: "))
for i in [n]:
    print("*"*n, end ="")


# c
for i in range(9):
    if i % 2 == 0:
        print("*", end ="")
    else:
        print("x", end ="")


# d
n = int(input("Enter number: "))
for i in range(n):
    if i % 2 == 0:
        print("*", end ="")
    else:
        print("x", end ="")

# f
for i in range(3):
    print()      
    for i in range(7):
        print("*",end ="")

# g
n = int(input("Enter number "))
m = int(input("Enter column "))
for i in range(m):
    print()      
    for i in range(n):
        print("*",end ="")
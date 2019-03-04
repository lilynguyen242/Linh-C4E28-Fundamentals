size = [5, 7, 300, 90, 24, 50, 75]
# 2.1
# print("Hello, my name is Linh and these are my sheep sizes")
# print(size, sep=", ")

# # 2.2
# print("Now my biggest sheep has size ", max(size), " let's shear it")

# # 2.3
# print("After shearing, here is my flock")
# i = size.index(max(size))
# size[i] = 8
# print(size)

# # 2.4
# print("One month has passed, now here is my flock")
# for i in range(0,len(size)):
#     size[i] += 50
# print(size)

# 2.5
print("Hello, my name is Linh and here is my flock")
print(size, sep=", ")
print("MONTH 1: ")
print("One month has passed, now here is my flock")
for i in range(0,len(size)):
    size[i] += 50
print(size)
print("Now my biggest sheep has size ", max(size), " let's shear it")
print("After shearing, here is my flock")
i = size.index(max(size))
size[i] = 8
print(size)
print()
print("MONTH 2: ")
print("One month has passed, now here is my flock")
for i in range(0,len(size)):
    size[i] += 50
print(size)
print("Now my biggest sheep has size ", max(size), " let's shear it")
print("After shearing, here is my flock")
i = size.index(max(size))
size[i] = 8
print(size)
print()
print("MONTH 3: ")
print("One month has passed, now here is my flock")
for i in range(0,len(size)):
    size[i] += 50
print(size)
print("Now my biggest sheep has size ", max(size), " let's shear it")
print("After shearing, here is my flock")
i = size.index(max(size))
size[i] = 8
print(size)

# 2.6
total = sum(size)
money = total*2
print()
print("My flock has ize in total: ", total)
print("I would get", total, "* 2$ = ", money, "$")
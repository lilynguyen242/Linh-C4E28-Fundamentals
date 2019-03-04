item = ["T-Shirt", "Sweater", "Short"]
print("Welcome to our shop, what do you want ? ")
# # Read
# print("Our items: ", end="")
# print(*item, sep=", ")

# # Create
# add = input("Enter new item: ")
# item.append(add)
# print("Our items: ", end="")
# print(*item, sep=", ")

# # Update
# a = int(input("Update position? "))
# b = input("New item? ")
# item[a-1] = b
# print("Our items: ", end="")
# print(*item, sep=", ")

c = int(input("Delete position? "))
del item[c-1]
print("Our items: ", end="")
print(*item, sep=", ")
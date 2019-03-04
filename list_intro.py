# list / array

# Create
# menu = ["Com", "Bun", "Pho", "Thit", "Rau"]
# menu.append("My")
# print(*menu, sep=", ")


# fav = ["anime", "netflix", "cooking"]
# print("Here is your favourite thing: ")
# print(*fav, sep=", ")
# n = input("Name one thing you want to add: ")
# fav.append(n)
# print(*fav, sep=", ")


# Read:
# loop with item
# for item in menu:
    # print(item)


# loop with index
# for index in range(len(menu)):
#     print(index, menu[index], sep=". ")

# loop with item, index
# for index, item in enumerate(fav):
#     print(index+1, item)


# # Update:
# menu[0] = "Chao"
# print(menu)


# Delete
menu = ["Com", "Bun", "Pho", "Thit", "Rau"]
# menu.pop(1)
del menu[2]
print(*menu)
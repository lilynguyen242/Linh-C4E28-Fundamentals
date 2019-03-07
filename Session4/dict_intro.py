# key: value
person = {
    "name": "Duc",
    "age": 22,
    "ex": 3,
    "language": "chinese"
}
name = person["name"]

# READ:

# for key in person.keys():
#     print(key)

# for value in person.values():
#     print(value)

# for key, value in person.items():
#     print(key, value)


# CREATE & UPDATE:
# person["age"] = 20
# print(person)


# DELETE:
del person["age"]
print(person)

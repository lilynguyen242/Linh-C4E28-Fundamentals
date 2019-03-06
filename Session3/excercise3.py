from random import choice
many_words = ["champion", "homework", "dungeon"]
word = choice(many_words)
random_list = []
list_word = list(word)
while len(list_word) > 0:
    char = choice(list_word)
    random_list.append(char)
    list_word.remove(char)
print(*random_list, sep=" ")


while True:
    user_word = input("Your answer: ")
    if user_word == word:
        print("Hura!!!")
        break
    else:
        print(":(")
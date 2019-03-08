loop1 =True
while loop1:
    print('''
    Answer the following algebra question:
    If x = 8, then what is the value of 4(x +3) ?
    1. 35
    2. 36
    3. 40
    4. 44 
    ''')
    count = 0
    n = int(input("Your choice: "))
    if n == 4:
        print("Bingo!!!")
        count += 1
    else:
        print(":(")
        loop1 = False
loop2 = True
while loop2:
    print('''
    Estimate this answer (exact calculation not needed):
    Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean ?
    1. About 55
    2. About 65
    3. About 75
    4. About 85
    ''')
    m = int(input("Your choice: "))
    if m == 2:
        print("Bingo!!!")
        count += 1
    else:
        print(":(")
    print("You correct answer", count, " out of 2 questions")
    break
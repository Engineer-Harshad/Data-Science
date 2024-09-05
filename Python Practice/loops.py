
# li = ["Daniel", 1, True, 3.2, "Wolfswagan", 78, 82.5]

# for item in li:
#     if str(item).isnumeric() and item > 6:
#         print(item)

# i = 11
# while(i<15):
#     print(i)
#     i = i + 1 

mynum = 20
Guess = range(1,5)
for chance in Guess:
    print("Total guesses: 5")
    i = int(input("Enter your number\n"))
    if i == mynum:
        print("Congrates! You have guessed right!")
        break
    elif i in range(1,10):
        print("Try little big one!")
    elif i in range(11,20):
        print("You are very close")
    elif i in range(21,30):
        print("Try lil smaller number")
    elif i in range(31,50):
        print("Reduce it ")
    elif i in range(51,100):
        print("This is big number, reduce more")
    Remaining = len(Guess) - chance
    print("No_of_guesses_left: " + str(Remaining))
    if chance == 0:
        print("Game Over")
    break

    
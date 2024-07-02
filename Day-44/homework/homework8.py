# 3) Write a while loop that asks the user to guess a number between 1 and 10 until they get it right. The correct number is 7.correct_number = 7

correct_num = 7
guess = 0

while guess != correct_num:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess != correct_num:
        print("Wrong guess. Try again!")

print("Congrats! You guessed the correct number")
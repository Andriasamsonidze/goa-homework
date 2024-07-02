# 5) Write a while loop that repeatedly asks the user to enter a password until the correct password "password123" is entered.

correct_pass = "password123"
entered_pass = ""

while entered_pass != correct_pass:
    entered_pass = input("type the password: ")
    if entered_pass != correct_pass:
        print("Incorrect password, please type password again.")

print("Thats correct! ")
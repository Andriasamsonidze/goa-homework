def numbers():
    question1 = int(input("Enter a random number: "))
    question2 = int(input("Enter a random number: "))
    if question1 % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"
    
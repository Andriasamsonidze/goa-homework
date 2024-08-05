# 1) შექმენით კალკულატორის ფუნქცია  რომელიც მომხმარებელს შეეკითხება ორ რიცხვს და მოქმედების 
# ტიპს(მიმატება, გამოკლება, გამრავლება, გაყოფა) შესაბამისად ფუნქცია 
# დააბრუნებს ანუ დაბეჭდავს შედეგს იმისდამიხედვით მომხმარებელს რა სურს და რა რიცხვები შემოიტანა, მაგალითად 
# მომხმარებელმა თუ შემოიტანა 5 და 2 და ასევე მას სურს გამრავლება ფუნქციამ უნდა დააბრუნოს დაბეჭდოს შედეგად 2 * 5 ანუ 10

def calculator():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    
    operation = input("Enter the type of operation (adding, subtracting, multiplicating, dividing): ")

    if operation == "adding":
        result = number1 + number2
        print(result)
    elif operation == "subtracting":
        result = number1 - number2
        print(result)
    elif operation == "multiplicating":
        result = number1 * number2
        print(result)
    elif operation == "dividing":
        if number2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = number1 / number2
            print(result)

calculator()

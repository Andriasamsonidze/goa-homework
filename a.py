def square_digits():
    num = input("Enter an integer: ")
    result = ""
    for digit in num:
        squared_digit = int(digit) ** 2
        result += str(squared_digit)
    return int(result)
print(square_digits())

# შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს ორ რიცხვს და დააბრუნებს მათ ჯამს.

def sum_of_the_numbers ():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sum = num1 + num2
    return sum
print("Sum of your numbers is", sum_of_the_numbers())
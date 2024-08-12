# შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს ორ რიცხვს და დააბრუნებს მათ ჯამს დამატებული 5.

def sum():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter the second number: "))
    sum = num1 + num2
    return sum + 5
print("The sum of the numbers plus five is",sum())
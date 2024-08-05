# 4) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს და 
# შემდეგ კი დააბრუნებს დაბეჭდავს მომხმარებლის შემოტანილი რიცხვი კენტია თუ ლუწი

def odd_even():
    number = int(input("Enter a number: "))
    
    if number % 2 == 0:
        print(number, "is an even number")
    else:
        print(number, "is an odd number")

odd_even()

# შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს რიცხვს და თუ ის დადებითი იქნება, დააბრუნებს "დადებითი", და თუ უარყოფითი იქნება, "უარყოფითი".

def Positive_or_Negative ():
    num = int(input("Enter a number: "))
    if num < 0:
        return "The number is negative"
    elif num > 0:
        return "The number is positive"
    else:
        return "The number is 0"
print(Positive_or_Negative())
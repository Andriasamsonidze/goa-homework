#შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს ორ ციფრს და დააბრუნებს მათ შორის უმცირესს.

def num ():
    num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
    num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
    if num1 > num2:
        return "მეორე რიცხვი ნაკლებია პირველზე"
    elif num1 < num2:
        return "პირველი რიცხვი ნაკლებია მეორეზე"
    else:
        return "ორივე რიცხვი ტოლია"
print(num())
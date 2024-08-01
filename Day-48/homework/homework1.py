#შევქმნათ ცარიელი სია, მომხმარებელს შევეკითხოთ 1000 ჯერ თუ რისი დამატება სურს სიაში

list = []

for i in range(1000):
    User_input = input("Enter anything that you would like to add to the list: ")
    list.append(User_input)

print("Your list has been created:")
print(list)
# 2) მომხმარებელს შემოატანინეთ რიცხვები, ამ რიცხვებისგან შექმენით სია შემდეგ კი დაითვალეთ რამდენი ორნიშნა რიცხვია სიაში

Number_list = []
Two__digit_number_list = []
for i in range(10):
    num = int(input("Enter a random number: "))
    Number_list.append(num)
for i in range(len(Number_list)):
    if Number_list[i] > 9 and Number_list[i] < 100:
        Two__digit_number_list.append(Number_list[i])
    else:
        continue
print("These are two digit numbers: ", Two__digit_number_list)
print(len(Two__digit_number_list))


# 1) მომხმარებელს შემოვატანინოთ 10 რიცხვი შემდეგ დავამატოთ სიაში, 
# გავფილტროთ ეს სია ორ ნაწილად ლუწებად და კენტებად და დავამატოთ 
# ახალ სიაში ლუწები ცალკე კენტები ცალკე

list = []
odd = []
even = []

for i in range(10):
    num = int(input("Type number: "))
    list.append(num)


for i in range(len(list)):
    if list[i] % 2 == 0:
        even.append(list[i])
    else:
        odd.append(list[i])

print("even numbers", even)
print("odd numbers", odd)
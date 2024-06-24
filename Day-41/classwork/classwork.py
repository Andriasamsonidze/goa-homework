#  1) გადმოგვეცემა რიცხვებით სავსე სია, ჩვენ უნდა შევქმნათ ახალი სია და ამ 
# სიაში უნდა დავამატოთ უკვე არსებული სიის ელემენტები შემოტრიალებული 
# სახით, reverse
# Original list of numbers

num = [1,2,3,4,5,6,7,8,9,0]
reverse_list = []
for i in range(len(num)):
    reverse_list.append(num[-i-1])
print("this will be the reversed list", reverse_list)

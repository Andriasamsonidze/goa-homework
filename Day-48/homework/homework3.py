#შევქმნათ ცარიელი სია, სიაში დავამატოთ, კიდევ 2 სია და გადავატაროთ for loop ში

list = []

list1 = [10, 20, 30]
list2 = [40, 50, 60]

list.append(list1)
list.append(list2)

for i in range(len(list)):
    sublist = list[i]
    print("Sublist", i + 1, ":", sublist)
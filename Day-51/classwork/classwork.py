# 1) შექმენით თავდაპირველა ცარიელი სია, შემდეგ ამ სიაში დაამაეთ 7 ელემენტი, ისევ ამ სიაში მესამე ინდექსზე მდგომ ელემენტს და მეორე 
# ინდექსზე მდგომ ელემენტს შეუცვლით ადგილებს,  მეოთხე ინდექსზე დაამატებთ ახალ დიდი რიცხვს, 
# ასევე მეხუთე ინდექსზე მდგომ ელემენტს და პირველივე ელემენტს ამოშლით სიიდან და დაბეჭდავთ განახლებულ სიას

list = []

for i in range(1,8):
    list.append(i)

second = list[2]
third = list[3]

list[2] = third
list[3] = second

list.insert(4, "andria")

list.remove(list[0])
list.remove(list[-1])

print(list)
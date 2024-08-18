# დაწერეთ ალგორითმი, რომელიც მომხმარებელს შეეკითხება რიცხვს. თუ 
# რიცხვი ლუწია გაყავით ორზე, სხვა შემთხვევაში გაამრავლეთ სამზე და მიუმატეთ ერთი.

num = int(input("Enter a number: "))

if num % 2 == 0:
    result = num // 2
else:
    result = num * 3 + 1

print("Result = ", result)

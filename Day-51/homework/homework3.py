# შექმენით რიცხვებით სავსე სია რომელშიც იქნება 1 დან 20 მდე ყველა რიცხვი, შემდეგ კი ამ სიიდან 
# ამოშალეთ ყველა კენტი რიცხვი და დაამატეთ ახალ სიაში, ორივე სია დაბეჭდეთ

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)


print("Original List:", numbers)
print("Odd Numbers List:", odd_numbers)

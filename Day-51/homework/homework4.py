# შექმენით სია რომელშიც იქნება 10 განსხვავებული რიცხვი შემდეგ კი დაბეჭდეთ ყველა ლისტის ელემენტის ჯამი

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0

for i in range(len(numbers)):
    sum += numbers[i]
print("The sum of all list elements is:", sum)
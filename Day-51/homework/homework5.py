# შექმენით რიცხვებით სავსე სია, გამოითვალეთ ამ სიის ელემენტების საშუალო არითმეტიკული 

sum = 0 
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20]
average = 0
for i in range (len(numbers)):
    sum = sum + numbers[i]
average = sum / len(numbers)

print("average numbers from 1 to 20" + str(average))
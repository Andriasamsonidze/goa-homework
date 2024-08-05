# 3) შექმენით ფუნქცია რომელშიც დააბრუნებს სიაში არსებული რიცხვების საშუალო არითმეტიკულკს

def Arithmetic():
    sum = 0 
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20]
average = 0
for i in range (len(numbers)):
    sum = sum + numbers[i]
average = sum / len(numbers)

print("average numbers from 1 to 20" + str(average))

Arithmetic()
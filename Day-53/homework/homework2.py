#  2) შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია და ფუნქცია დააბრუნებს ამ რიცხვების ჯამს

def sum(): 
    sum = 0
    numbers = [1,5,3,6,7,8,3,67,2,6]
    for i in range (len(numbers)):
        sum = sum + numbers[i]
    print("The sum of numbers is " + str(sum))

sum()
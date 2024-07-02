# 4) Enter a number to the user and then using a for loop output the sum of all the numbers up to this 
# number (for example, if he enters 10, output the sum of all the numbers up to 10, for example).

num = int(input("enter a number: "))
sum = 0
for i in range(num):
    sum += i
print(sum)
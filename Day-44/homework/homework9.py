#4) Write a while loop that processes a list of numbers, doubling each number, and prints the new list.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled_numbers = []
sum = 0

while sum < len(num):
    doubled_numbers.append(num[sum] * 2)
    sum += 1

print("Original list:", num)
print("Doubled list:", doubled_numbers)
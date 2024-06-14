odd_list = []
even_list = []

num = int(input("Enter a number: "))

if num % 2 == 0:
    even_list = even_list = [num]
else:
    odd_list = odd_list + [num]

print("odd list", odd_list)
print("even list", even_list)



Less = []
More = []


for i in range(10):
    input_num = int(input("Enter a random number: "))
    if input_num == 100:
        continue
    elif input_num < 100:
        Less.append(input_num)
    else:
        More.append(input_num)
print("These numbers are more than 100", More)
print("These numbers are less than 100", Less)
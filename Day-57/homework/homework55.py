#Create a script that uses a while loop to iterate over a list.

list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = 0

while index < len(list):
    print("Elements index", index, "is:", list[index])
    index += 1
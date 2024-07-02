# 1) შევქმნათ სია რომელშიც გვექნება რომელშიც გვექნება დადებითი და უარყოფითი რიცხვები. გავფილტროთ, უნდა დავაბრუნოთ ორი სია ერთში მხოლოდ დადებითი რიცხვები მეორეში მხოლოდ უარყოფითი რიცხვები

numbers = [4, -2, 43, 20, -48, 23, 69, -26]
possitive_nums = []
negative_nums = []
for i in range (len(numbers)):
    if numbers[i] == 0:
        continue
    elif numbers[i] <0:
        negative_nums.append(numbers[i])
    else:
        possitive_nums.append(numbers[i])
print("these are negative numbers: ", possitive_nums)
print("these are negative numbers: ", negative_nums)

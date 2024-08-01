word_list = []

while True:
    word = input("შეიყვანეთ სიტყვა რომელიც 6ს ასოს არ აღემატება: ")
    if len(word) <= 6:
        word_list.append(word)
    else:
        print("სიტყვა ზედმეტად გრძელია სცადეთ ახლიდან: ")






print(word_list)
# შექმენი ფუნქცია, რომელიც შემოატანინებს მომხარებელს ტექსტს და დააბრუნებს ტექსტის სიგრძეს.

def len_text():
    text = input("Write a text: ")
    return len(text)
print("The size of text is", len_text(), "letters")
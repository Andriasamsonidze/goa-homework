# შექმნი ფუნქცია, რომელიც იღებს number პარამეტრს და აბრუნებს "დიდია" თუ number 10-ზე მეტია და "პატარა" თუ ნაკლებია. 
# მაგალითად, გამოიყენე არგუმენტი 9. (გამოიტანა: "პატარა")

def small_big(number):
    if number > 10:
        return "bigger"
    else:
        return "smaller"
print(small_big(25))
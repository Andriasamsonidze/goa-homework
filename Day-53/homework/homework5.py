# 5) შექმენით დროში მოგზაურობის ფუნქცია რომელიც მომხმარებელს შეეკითხება მის ახლანდელ ასაკს და ამჟამინდელ წელს, 
# ასევე რამდენი ხნით სურს დროში მოგზაურობა შემდეგ კი ფუნქციამ უნდა დააბრუნოს დაბეჭდოს დროში მოგზაურობის შემდეგ რომელი წელი იქნება 
# და რამდენი წლის იქნება მომხმარებელი, ასევე დაამატეთ რომ მომხმარებელმა მიიღოს გადაწყვეტილება წარსულში სურს დრში მოგზაურობა თუ მომავალში


def time_travel():
    current_year = int(input("Enter the current year: "))
    current_age = int(input("Enter your current age: "))
    travel_years = int(input("Enter how many years you want to travel: "))
    direction = input("Do you want to travel in the future or in the past? ")

    if direction == "past":
        future_year = current_year - travel_years
        future_age = current_age - travel_years
    elif direction == "future":
        future_year = current_year + travel_years
        future_age = current_age + travel_years

    print()

time_travel()

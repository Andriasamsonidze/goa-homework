# შექმენით ოთხი მათემატიკური ფუნქცია, თითოეულს გადაეცით ორი არგუმენტი და სახელის შესაბამისად მოახდინეთ მუშაობა. ოპერაციები: +, -, *, /

def add(A, S):
    return A + S

def subtract(A, S):
    return A - S

def multiply(A, S):
    return A * S

def divide(A, S):
    if S != 0:
        return A / S
    else:
        return "Can't divide by zero"

#Q1
def welcome():
    print("Welcome to Python")

welcome()
welcome()
welcome()


#Q2
def greet(name):
    print("Hello", name)

greet("Keshav")


#Q3
def show_number(number):
    print(number)

show_number(25)


#Q4
def add(a, b):
    return a + b

print(add(10, 20))

def add(a,b):
    return(a+b)
print(add(1,2))



#Q5
def square(number):
    return number ** 2

print(square(5))


#Q6
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(8))
print(is_even(7))


#Q7
def get_full_name(first_name, last_name):
    return first_name + " " + last_name

print(get_full_name("Keshav", "Raj"))


#Q8 ai
def introduce(name, city="Pune"):
    print("My name is", name, "and I live in", city)

introduce("Keshav")
introduce("Keshav", "Ahmedabad")


#Q9
def subtract(a, b):
    return a - b

print(subtract(10, 5))
print(subtract(5, 10))


#Q10
def get_min_max(a, b):
   
    if a > b:
        return f"{a} is larger and {b} is smaller"
    elif a < b:
        return f"{b} is larger and {a} is smaller"
    else:
        return "Both numbers are equal"

print(get_min_max(10, 20))

print(get_min_max(10, 20))


#Q11
def calculate(a, b):
    return a + b, a - b, a * b, a / b

print(calculate(10, 5))


#Q12 ai
def count_digits(number):
    if number == 0:
        return 1
    count = 0
    while number > 0:
        number = number // 10
        count += 1
    return count

print(count_digits(12345))


#Q13
def classify_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(classify_number(10))
print(classify_number(-5))
print(classify_number(0))


#Q14
def calculate_total(price, quantity=1):
    return price * quantity

print(calculate_total(100))
print(calculate_total(100, 3))


#Q15 ai
def create_email(username, domain="example.com"):
    return username + "@" + domain

print(create_email("keshav"))
print(create_email("keshav", "gmail.com"))
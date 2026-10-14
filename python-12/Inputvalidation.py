#Q1
marks = int(input("Enter marks :"))
while 0 <= marks >= 100:
    marks = int(input("Enter marks"))

print(marks)


# Q2
n = int(input("Enter a positive integer: "))
while n <= 0:
    n = int(input("Enter a positive integer again: "))
print(n)


# Q3
age = int(input("Enter your age: "))
while age < 0 or age > 120:
    print("Invalid age!")
    age = int(input("Enter your age again: "))
print(age)


# Q4
print("1. View profile")
print("2. Edit profile")
print("3. Settings")
print("4. Exit")

choice = int(input("Enter your choice: "))
while choice < 1 or choice > 4:
    choice = int(input("Enter a valid choice: "))
print("Selected option:", choice)


# Q5
# password = input("Enter a password: ")
# while len(password.strip()) < 8:
#     password = input("Password must contain at least 8 characters. Enter again: ")
# print("Password accepted!")

password = input("Enter your password :")
while len(password.strip()) < 8:
    password = input("Password must contain at least 8 characters. ")
print("Password accepted!")


# Q6
temperature = int(input("Enter temperature: "))
while temperature < -20 or temperature > 45:
    temperature = int(input("Enter temperature between -20 and 45: "))
print("Accepted temperature:", temperature)


# Q7
balance = 5000
amount = int(input("Enter withdrawal amount: "))
while amount <= 0 or amount > balance:
    amount = int(input("Invalid amount. Enter withdrawal amount again: "))
balance -= amount
print("Remaining balance:", balance)


# Q8
username = input("Enter username :").strip()

while len(username) < 5 or username == "" or username == " ":
    username = input("Wrong username try again :")
print("Correct username".strip())



# Q9
n = int(input("Enter a positive integer divisible by 3 and 5: "))
while n <= 0 or n % 3 != 0 or n % 5 != 0:
    n = int(input("Invalid number. Enter again: "))
print("Accepted number:", n)


# Q10
security_pin=2468
attempt = 0

while attempt < 3:
    pin = int(input("Enter PIN :"))
    if pin == security_pin:
        print("Access granted")
        break
    attempts+=1
    print("Try again")
else:
    print("Access denied")




# Q11
n = int(input("Enter an integer between 10 and 50: "))
while n < 10 or n > 50:
    n = int(input("Invalid number. Enter an integer between 10 and 50: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q12
balance = 2000
deposit = int(input("Enter deposit amount: "))
while deposit <= 0:
    deposit = int(input("Invalid amount. Enter a positive deposit: "))
balance += deposit
print("New balance:", balance)



# Q13
n = int(input("Enter an integer between 1 and 100: "))

while n < 1 or n > 100:
    n = int(input("Invalid number. Enter again: "))

print("Accepted number:", n)


# Q14
marks = int(input("Enter marks: "))

while marks < 0 or marks > 100:
    marks = int(input("Invalid marks. Enter again: "))

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")


# Q15
username = input("Enter username: ").strip()
password = input("Enter password: ")

while len(username) < 5 or " " in username or len(password.strip()) < 8:
    print("Invalid username or password. Try again.")
    username = input("Enter username: ").strip()
    password = input("Enter password: ")

print("Username and password accepted!")


# Q16
a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")

while operator not in ["+", "-", "*", "/"]:
    operator = input("Invalid operator. Enter again (+, -, *, /): ")

b = float(input("Enter second number: "))

while operator == "/" and b == 0:
    b = float(input("Cannot divide by zero. Enter second number again: "))

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
else:
    result = a / b

print("Result:", result)


# Q17
balance = 10000

while True:
    print("\n1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current balance:", balance)

    elif choice == 2:
        deposit = float(input("Enter deposit amount: "))

        while deposit <= 0:
            deposit = float(input("Enter a positive deposit amount: "))

        balance += deposit
        print("New balance:", balance)

    elif choice == 3:
        withdraw = float(input("Enter withdrawal amount: "))

        while withdraw <= 0 or withdraw > balance:
            withdraw = float(input("Invalid amount. Enter again: "))

        balance -= withdraw
        print("New balance:", balance)

    elif choice == 4:
        print("Thank you for using the banking system!")
        break

    else:
        print("Invalid choice. Select 1, 2, 3, or 4.")


# Q18
month = int(input("Enter month (1-12): "))
day = int(input("Enter day (1-31): "))

while month < 1 or month > 12 or day < 1 or day > 31:
    print("Invalid month or day. Try again.")
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))

print("Accepted month:", month)
print("Accepted day:", day)


# Q19
quantity = int(input("Enter product quantity: "))

while quantity <= 0:
    quantity = int(input("Quantity must be positive. Enter again: "))

price = float(input("Enter unit price: "))

while price <= 0:
    price = float(input("Price must be greater than zero. Enter again: "))

total = quantity * price

print("Total cost:", total)


# Q20
count = int(input("How many numbers do you want to enter (1-20)? "))

while count < 1 or count > 20:
    count = int(input("Invalid count. Enter a number from 1 to 20: "))

total = 0

for i in range(count):
    number = float(input("Enter a number: "))
    total += number

average = total / count

print("Average:", average)


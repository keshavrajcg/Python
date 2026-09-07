#Q1
name=input("Enter your name:")
print("My name is " , name)

#Q2
city=input("Enter your city:")
print("I live in " , city)

#Q3
name=input("Enter your name:")
age=input("Enter your age:")
print("My name is" , name , "and my age is" , age)

#Q4
#By default input() function takes input as string. 
#If we want to take input as integer then we have to use int() function with input() function.

#Q5
value=input("Enter value:")
print(type(value)) #it will print <class 'str'>

#Q6
first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
print(f"My first name is , {first_name} , and my last name is , {last_name}")

#Q7
name=input("Enter your name:")
city=input("Enter your city:")
college=input("Enter your college name:")
print(f"My name is {name} , I live in {city} , and I study in {college}")

# #Q8
# name1=input("Enter your name:")
# name2=input("Enter your friend's name:")
# print(name1.split() , name2.split())

#Q8
name1 , name2 = input("Enter two names :").split()
print("First name is " , name1)
print("Second name is " , name2)

#Q9
program,language=input("Enter :").split()
print("First word is " , program)
print("Second word is " , language)

#Q10
a,b,c=input("Enter three values :").split()
print("First value is " , a)
print("Second value is " , b)   
print("Third value is " , c)

#Q11
a="25"
print(int(a))
print(type(int(a)))

#Q12
b="25.5"
print(float(b))
print(type(float(b)))

#Q13
c=100
print(str(c))
print(type(str(c)))

#Q14
d=input("Enter a number:")
print(type(int(d)))

#Q15
e=float(input("Enter a number:"))
print(type(e))

#Q16
a = input()
b = input()
print(a + b)
#The input() function in Python always returns data as a string (str), even if the user enters digits.Because it is default of input.

#Q17
a = input("Enter first number: ")
b = input("Enter second number: ")
print(int(a) + int(b))

#Q18
name="Rahul"
age=20
print(f"my name is , {name} , and my age is {age}")

#Q19
a=10
b=20
print(f"{a+b}")

#Q20
user_name=input("Enter your name :")
user_age=input("Enter your age:")
print(f"my name is, {user_name} , and my age is , {user_age}")

#Q21
price_product=float(input("Enter price of the product: "))
print(f"{price_product:.2f}")

#Q22
#:.2f is used to set limit.

#Q23
product_name=input("Enter name of the product:")
product_price=input("Enter product price:")
product_quantity=input("Enter product quantity:")
print(f"Your product is {product_name} , it's price is {product_price} and it's quantity is {product_quantity}")

#Q24
print("A", "B", "C")
#it will simply display the result as A B C.

#Q25
print("2026", "08", "19", sep=("-"))

#Q26
print("hello", end="")
print("world")

Q27
a,b=map(int,input("enter first no. annd second no.").split()[:2])
print(f"This is fist {a} and thhis is second no. {b}")

#Q28
price=int(input("enter the price"))
quantity=int(input("enter quantity"))
print(f"total = {price * quantity}")

#Q29
student_name=input("enter name:")
student_age=(int(input("enter age:")))
student_marks=(float(input("enter marks:")))
print("name is", student_name , "age is" , student_age , "marks is " , student_marks)

#Q30
s_name=input("Enter name:")
s_age=int(input("Enter age:"))
s_height=float(input("Enter height:"))
city=input("Enter city:")
print(f"Student name = {s_name} , Student's age= {s_age} , Student's height = {s_height :.2f} and city is = {city}")
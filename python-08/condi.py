#Q1
number=int(input(20))
if number >= 10:
    print("Greater than 10")

#Q2
age = int(input(21))
if age >= 18:
    print("This person is adult")

#Q3
number=int(input("enter a no."))    
if number >= 0:
    print("Positive")

#Q4
marks=int(input("Enter marks:"))    
if marks >= 40:
    print("Pass")

#Q5    
no=int(input("Enter a number:"))
if no == 0:
    print("Zero")

#Q6
number=int(input("Enter a number:"))
if number >= 0:
    print("Positive")
else: print("Negative") 

#Q7
age= int(input("Enter your age:"))
if age >= 18:
    print("Adult")
else: print("Minor")

#Q8
integer=int(input("Enter a no.:"))
if integer % 2 ==0:
    print("Even")
else: print("Odd")

#Q9
marks=int(input("Enter marks:"))
if marks >= 40:
    print("pass")
else:print("fail")

#Q10
no1 = int(input("Enter first number:"))
no2 = int(input("Enter second number:"))
if no1 >= no2:
    print("Greater than")
else:print("Less than")

Q11
marks=int(input("Enter marks:"))
if marks >= 90:
    print("A")
elif marks >= 75 :
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:print("F")

Q12
num=int(input("Enter a number:"))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:print("Zero")

#Q13
week=int(input("Enter a number between 0 to 6 :"))
if week == 1:
    print("Monday")
elif week == 2:
    print("Tuesday")
elif week == 3:
    print("Wednesday")
elif week == 4:
    print("Thursday")
elif week == 5:
    print("Friday")
else:print("Other")

#Q14
marks=int(input("Enter marks:"))
if marks >=90:
    print("Excellent")
elif marks >=75:
    print("Good")
elif marks >=40:
    print("Pass")
else:print("Fail")


#Q15
num=int(input("Enter a number:"))
if num == 1:
    print(1)
elif num == 2:
    print(2)
elif num == 3:
    print(3)
else:print("Other")

#Q16
age=int(input("Enter age:"))
if age >=18:
   print("Atleast above 18")
   if age <= 60:
    print("Age is between 18 and 60")
   else:print("Must be less than 60")

#Q17
marks=int(input("Enter marks: "))
if marks >= 75:
    print("Good")
elif marks >= 40:
    print("Passed")
else: print("Failed")

#Q18
no_=int(input("Enter a number"))
if no_ >0:
    print("Number is positive")
    if no_ >100:
        print("and greater than 100")

#Q19
age=int(input("Enter age :"))
if age >=18 :
    if age >= 60:
        print("Age falls under senior citizen")
    else:
        print("Age of an adult.")
else:print("Age is of a minor")

#Q20
b=int(input("Enter a number:"))
if b !=0:
    if b > 0:
        print("Positive")
    if b<0:
            print("Negative")
if b == 0:
     print("Neither positvie nor negative")

#Q21
m=int(input(("Add age :")))
marks=int(input("Add marks :"))
if m >= 18 and marks >=40:
     print("Eligible")
else:print("Not eligible")

#Q22
a=int(input("write a number :"))
if a <10 or a > 100 :
     print("Speical")
else:print("Between 10 and 100")

#Q23
has_id= input("Do you have id? (True/False)")
age=int(input("Enter age"))
if age >= 18 and has_id is True:
     print("Allowed")
else:print("not allowed")


age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"
if age >= 18 and has_id is True:
    print("Allowed")

#Q24
first_number=int(input("Enter first number :"))
second_number=int(input("Enter second number:"))
if first_number>10 and second_number>10:
    print("Both are greater than 10")

#Q25
nnum=int(input("Enter a number :"))
if nnum < 0 or nnum > 100:
    print("nub is out side of 0 to 100")

#26

#27
c=int(input("Inser a Number :"))
if c >10 and c < 50:
    print("Number is in between 10 and 50")

#Q28
d=int(input("Enter a num :"))
if d <10 or d > 50:
    print("Outside the range of 10 and 50")

#Q29
is_student=input("Yes/No").lower() 
has_id=input("Yes/No").lower() 
has_ticket=input("Yes/No").lower() 
if is_student == "yes":
    if has_id == "yes":
        if has_ticket == "yes":
            print("Allowed")

#using and
is_student = input("Are you a student? (Yes/No): ").lower() == "yes"
has_id = input("Do you have an ID? (Yes/No): ").lower() == "yes"
has_ticket = input("Do you have a ticket? (Yes/No): ").lower() == "yes"
if is_student and has_id and has_ticket:
    print("Allowed")

#Q30
age=int(input("Enter age :"))
marks=int(input("Enter marks :"))
has_id=input("Has id (yes/no)").lower() 
if age >= 18 and marks >= 40 and has_id == "yes":
    print("Eligible")
else:print("Not eligible")
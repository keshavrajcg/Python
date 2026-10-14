# #Q1
# n = int(input("Enter a number :"))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")

# #Q2
# a=int(input("Enter a number :"))
# b=int(input("Enter second number :"))
# if a>b:
#     print("Bigger number is",a)
# else:
#     print("Bigger number is ",b)

# #Q3
# a=int(input("Enter 1st number :"))
# b=int(input("Enter 2nd number :"))
# c=int(input("Enter 3rd number :"))
# if a>b>c and a>c>b:
#     print("Largest number is" ,a )
# elif b>c>a and b>a>c:
#     print("Largest numbere is " ,b)
# else:
#     print("Largest number is",c)

# #Q4
# p=int(input("Enter a number :"))

# if p>0:
#     print("Positive number ")
# elif p<0:
#     print("Negative number ")
# else:
#     print("Zero")

#Q5
age=int(input("Enter age :"))
if age >=0 and age<=12:
    print("Child")
elif age>=13 and age<=19:
    print("Teenager")
    
else:
    print("Adult")

#Q6
marks=int(input("Enter marks :"))
if marks >=90 and marks<=100:
    print("A Grade")
elif marks >=80 and marks <90:
    print("B Grade")
elif marks >=70 and marks <80:
    print("C Grade")
elif marks >=60 and marks <70:
    print("D Grade")
elif marks >=0 and marks <60:
    print("F Grade")
else:
    print("Invalid")

#Q7
number = int(input("Enter a number :"))
if number %5==0:
    print("Number is divisible by 5")
else:
    print("Not divisible by 5")

#Q8
both = int(input("Enter a number :"))
if both %5==0 and both % 3==0 :
    print(f"This number {both}, is both divisible by 5 & 3")
else:print("Not divisible by both 3 and 5")

#Q9
year = int(input("Enter a year :"))
if year %4==0:
    print("It's a leap year")
else:print("Not a leap year")

#Q10
n=int(input("Enter a number :"))
if n >10 and n <50:
    print("In range")
else:print("Out of range")
# # a=int(input("Enter a number: "))
# # if a > 0:
# #     print("Positive")
# # if a < 0:
# #     print("Negative")
# # if a == 0:
# #     print("Zero")

# # #Q2
# # b=int(input("Enter a number : "))
# # if b > 0 and b % 2 == 0:
# #     print("Positive Even")
# # if b > 0 and b % 2 != 0:
# #         print("Positive Odd")
# # if b <0 and b % 2 == 0:
# #             print("Negative Even")
# # if b <0 and b %2 != 0:
# #                 print("Negative Odd")
# # if b == 0:
# #         print("Zero")

# # #Q3
# # a,b=map(int,input("Enter two numbers : ").split())
# # if a>b:
# #         print("First number is greater")
# # if a<b:
# #         print("Second number is greater")
# # if a==b:
# #         print("Both numbers are equal")

# # #Q4
# # one=int(input("Enter first number :"))
# # two=int(input("Enter second number :"))
# # three=int(input("Enter third number :"))

# # if one > two > three:
# #         print("Third number is the smallest")
# # if two > one > three:
# #         print("Third number is the smallest")
# # if two > three > one:
# #         print("First number is the smallest")
# # if three > two > one:
# #         print("First number is the smallest")
# # if one > three > two:
# #         print("Second number is the smallest")
# # if three > one > two:
# #         print("Second number is the smallest")

# # #Q5
# # a=int(input("Enter first number :"))
# # b=int(input("Enter second number :"))
# # c=int(input("Enter third number :"))

# # if a > b > c:
# #     print( a, "is the largest")
# # if a > c > b:
# #        print(a , "is the largest")
# # if b > a > c:
# #        print(b,"is the largest")
# # if b > c > a:
# #     print(b, "is the largest")
# # if c > a > b:
# #     print(c,"is the largest")
# # if c > b > a:
# #     print(c,"is the largest")

# # #Q6
# # a=int(input("input a number :"))
# # if a % 5 ==0 and a % 11 == 0:
# #     print("The given number is divisible by 5 and 11")
# # elif a % 5 ==0:
# #       print("Number is only divisible by 5")
# # elif a % 11 ==0:
# #       print("Number is only divisible by 11")
# # elif a % 5 != 0 and a % 11 !=0:
# #       print("Divisible by neither 5 and 11")

# # #Q7
# # a=int(input("input a number :"))
# # if a % 3 ==0 and a % 7 == 0:
# #     print("The given number is divisible by 3 and 7")
# # if a % 3 == 0:
# #       print("Number is only divisible by 3")
# # elif a % 7 ==0:
# #       print("Number is only divisible by 7")
# # elif a % 3 !=0 and a % 7 !=0:
# #       print("Divisible by neither 3 and 7")

# # #Q8
# # marks=int(input("Enter marks :"))
# # if marks > 100:
# #       print("Invalid marks")
# # if marks >= 40:
# #       print("Pass")
# #       if marks <40:
# #               print("Fail")
         
# # if marks < 0:
# #       print("Invalid marks")

# #Q9
# marks=int(input("Enter marks :"))
# if marks > 100:
#       print("Invalid marks")
# if marks >= 90:
#       print("A Grade")
# elif marks >= 80:
#       print("B Grade")
# elif marks >= 70:
#       print("C Grade")
# elif marks >=60:
#       print("D Grade")
# elif marks >=40:
#       print("E Grade")
# elif marks <0:
#       print("Invalid marks")
# else:
#       print("Fail")

# #Q10
# age=int(input("Enter age :"))
# if age > 120:
#       print("Invalid age")
# elif age <0:
#       print("Invalid age")
# elif age <18:
#       print("Cannot not vote")
# elif age >=18:
#       print("Can vote")

# #Q11
# year=int(input("Enter a year : "))
# if year % 400 ==0 or year != 100 and year %4 ==0:
#       print("it's a leap year")
# else:print("Not a leap year")

# #Q12
# chr=input("Enter a character :")
# if chr >= "A" and chr <='Z':
#     print("UPPER CASE CHARACTER")
# if chr >='a' and chr <='z':
#     print("lower case character")
# if chr >= "-9" and chr <= "+9":
#     print("Digit it is") 
# else:print("Speical character")    

# #Q13
# alp=input("Enter a letter :")
# if alp =="a" or alp=="e" or alp=="i" or alp=="o" or alp =="u":
#     print("Vowel")
# else:print("Consonent")

# #Q14
# cost_price=int(input("Input cost price :"))
# selling_price=int(input("Input selling price :"))
# if cost_price < selling_price:
#     print("Profit ")
# if selling_price < cost_price:
#     print("Loss")
# elif cost_price == selling_price:
#     print("No profit and no loss")

# #Q15
# cost_price=int(input("Enter cost price"))
# selling_price=int(input("Enter selling price"))
# if selling_price > cost_price:
#     print("Profit is equal to" ,selling_price-cost_price , "Profit % ; is " , (selling_price-cost_price)/selling_price*100)
# elif selling_price < cost_price:
#     print("Loss is equal to", cost_price-selling_price , "Loss % ; is " , (cost_price- selling_price)/cost_price*100)
# else:print("Zero")

# #Q16
# bill=int(input("Enter electricity bill :"))
# if bill <100 and bill >0:
#     print("The bill is" ,bill*5 )
# elif bill <= 200 :
#     print("The bill is " , bill*7)
# elif bill >= 200:
#     print("The bill is " , bill*10)

# #Q17
# a=int(input("Enter first number :"))
# b=int(input("Enter second number :"))
# c=input("Select one of the operator \n" "+ \n" "- \n" "*\n" "/\n" )
# if c == "+":
#     print(a+b)
# elif c=="-":
#     print(a-b)
# elif c== "*":
#     print(a*b)
# elif c=="/" and b != 0:
#     print(a/b)

# #Q18
# temp=int(input("Enter temperature celsius :"))
# if temp > 35:
#     print("Hot")
# elif temp > 25:
#     print("Normal")
# elif temp > 15:
#     print("Cold")
# elif temp > -1:
#     print("Very cold")
# elif temp < 0:
#     print("Freezing")

# #Q19
# no=int(input("Enter a number :"))
# if no > 100:
#     print("This number is above 100")
# elif no >50:
#     print("This number is between 51-100")
# elif no >10:
#     print("This number is between 11-50")
# elif no >-1:
#     print("This number is between 0-10")

# #Q20
# p=int(input("Enter 1st number :"))
# q=int(input("Enter 2nd number :"))
# r=int(input("Enter 3rd number :"))

# if p+q>r and p+r>q and q+r>p:
#     print("Can form a triangle")
# else:print("Can't form a triangle")

# #Q21
# a=int(input("Enter 1st side :"))
# b=int(input("Enter 2nd side :"))
# c=int(input("Enter 3rd side :"))
# if a <0 or b<0 or c<0 or a+b+c<0 or a==b==c==0 or a+b<c or a+c<b or b+c<a:
#     print("Triangle cannot be formed")
# elif a==b==c:
#       print("Equilateral triangle")
# elif a==b!=c or a==c!=b or b==c!=a:
#       print("Isosceles")
# elif a!=b!=c:
#       print("Scalene")

# # account_balance=int(input("Enter account balance  :₹"))

# withdrawal_amount=int(input("Enter withdrawal amount :₹"))

# if withdrawal_amount<0:

#       print("Withdrawal amount be greater than zero ")

#       if withdrawal_amount%100==0:

#             print("Withdrawal amount must be divisible by hundred")

#             if withdrawal_amount>account_balance:

#                   print("Invalid")

#                   if account_balance-withdrawal_amount<500:

#                         print("Left balance cannot be less than ₹500")

# elif:print("Withdrawl sccessful \n" , "Reamaning balance :" ,account_balance-withdrawal_amount )

#Q22
account_balance=int(input("Enter account balance  :₹"))
withdrawal_amount=int(input("Enter withdrawal amount :₹"))

if withdrawal_amount < 0 and account_balance <0:
    print("Withdrawal amount must be greater than zero")

elif withdrawal_amount % 100 != 0:
    print("Withdrawal amount must be divisible by hundred")

elif withdrawal_amount > account_balance:
    print("Withdrawal amount cannot be greater than balance")

elif account_balance - withdrawal_amount < 500:
    print("Left balance cannot be less than ₹500")

else:
    print("Withdrawal successful")
    print("Remaining balance :", account_balance - withdrawal_amount)

#Q23
user_name=input("Enter username :")
user_password=input("Enter password :")

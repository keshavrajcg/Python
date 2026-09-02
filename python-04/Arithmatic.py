#Q1
a=4
b=6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#Q2
a=3
b=9.5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print(type(a))

#Q3
subject_1=80
subject_2=84
subject_3=91
print(subject_1+subject_2+subject_3)
print((subject_1+subject_2+subject_3)/3)

#Q4
product_price=100
quantity=5
print(product_price*quantity)

#Q5
a=7
print(a%2) #If the remainder is 0 then the value is Even and if the remainder is 1 then the value is Odd

#Q6
a=4
b=9
print(a/b)
print(a//b)
print((a/b)/2)
print((a//b)/2)

#Q7
a=-3
b=-8
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#Q8
a=10
b=-5
c=6
d=-2
print(a-c)
print(a-b)
print(b-a)
print(b-d)

#Q9
a=8
b=-2
c=4
d=-3
print(a//c)
print(b//a)
print(a//d)
print(b//d)

#Q10
a=3
b=2
c=-5
d=-1
print(a%b)
print(c%a)
print(b%d)
print(c%d)

#Q11
print(10+5*2)
print(20-4/2)
print(10+20/5*2)
print(2+3*4**2)
print(100-20//5) #Python followed the Operator Order and performed ** and *,/ first

#Q12
print(10+5*2)
print((10+5)*2)

print(20-10/2)
print((20-10)/2)

print(2+3*4)
print((2+3)*4) #The pritority of parentheses is highest among all the operators

#Q13
a=True
b=False
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print(type(a+b)) #Error will occur as division by zero is not defined

#Q14
a=True
b=False
print(a+5)
print(b+5)
print(a*10)
print(b*10)
print(a-5)
print(b-5) #Python treats True as 1 and False as 0 that is why we get these results.

#Q15
a="Jonny"
b="cage"
print(a+" "+b)

#Q16
a="Sumit"
b=3
c=4.3
print(a*b)
print(a*c) #We get TypeError: can't multiply sequence by non-int of type 'float'

#Q17
a="Bleep"
b="2"
print(a+b)
print(a-b)
print(a*b)
print(a/b) #Only addition works

#Q18
a=None
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b) #None is a empty or void quantity so, it will now produce any result.

#Q19
a=0
b=4
c="Zorko"
d="8"
e=None
print(b/a)
print(c*d)
print(a-e)

#Q20
a=3
b=-5
print("Addition:",a+b)
print("Substraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Floor Division:",a//b)
print("Modulus:",a%b)
print("Exponentiation:",a**b)

#21
a = 10
b = -3
c = 2.5
print(a+b)
print(a-c)
print(a*b)
print(a/b)
print(c//b)
print(a%c)
print(a**b)
print(a+(b))
print(c-b)
print(a*(b))
print(a/c)
print(a//b)
print(c%b)
print(a**c)
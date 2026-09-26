#Q1
for a in range(5):
    print("hello")

#Q2
for i in range(1,10):
    print(i)

#Q3
for i in range(1,10):
    print(i+1)

#Q4
for i in range(10,0,-1):
    print(i)

#or
for i in reversed(range(1, 10)):
    print(i)

#Q5
for i in range(5,51,5):
    print(i)

#Q6
for i in range(2,21):
    if i%2==0:
        print(i)

#Q7
for i in range(1,20):
    if i%2!=0:
        print(i)

#Q8
for i in range(1,20):
    if i%3==0:
        print(i)

#Q9
for i in range(20,1,-2):
    print(i)

#Q10
num=int(input("Enter a number :"))
for num in range(0,num):
    print(num+1)

#Q11
n=int(input("Enter a number :"))
for n in range(1,n):
    if n%2==0:
        print(n)

#Q12
n=int(input("Enter a number :"))
for n in range(0,n):
    if n%2!=0:
        print(n)

#Q13
n=int(input("Enter a number :"))
for n in range(1,n):
    if n%3==0:
        print(n)

#Q14
num=int(input("Enter a number :"))
for num in range(1,num):
    if n%2==0 and n%3==0:
        print(num)

#Q15
nun=int(input("Enter a number :"))
for nun in range(1,nun):
    if nun%2==0:
        print(nun)

#Q16
nn=int(input("Enter a number :"))
for i in range(1,nn+1):
    nn=nn+i
print(nn)

#Q17
n=int(input("Enter a number :"))
sum=0

for i in range(1,n+1):
    if i%2==0:
     sum= sum+i
print(sum)
    
#Q18
n=int(input("Enter a number :"))
sum=0

for i in range(1,n+1):
    if i%2!=0:
     sum= sum+i
print(sum)

#Q19
muber=int(input("Enter a number :"))
for i in range (1,11):
   print(muber*i)

#Q20
n=1
number=int(input("Enter a number :"))
for i in range(1,number +1):
    n=n*i
print(n)

#Q21
chracter=input("Enter a character :")
for i  in chracter:
    print(i)

#Q22
word=input("Enter a word :") 

for i in word:
    print(i, end="")

#Q23
character=input("Enter a chr :")
count=0
for i in character:
    count=count+1
print("Characters ; " , count)

#Q24
appears=input("Enter a string :")
count=0

for character in appears:
    if character=="a":
        count=count+1
print("Count:" , count)

#Q25
user=input("Enter a word :")
count=0

for upper in user:
    if upper.isupper():
        count +=1
        print("Number of uppercase letters:", count)

#Q26
for row in range(3):
    for column in range(4):
        print("*" , end="")
    print()

#Q27
for row in range(4):
    for column in range(5):
        print("*" , end="")
    print()

#Q28
for row in range(1,6):
    for column in range(1, row +1):
        print("*", end="")
    print()

#Q29
for row in range(1,6):
    for column in range(1,row+1):
        print(column , end="")
    print()

#Q30
for row in range(1,6):
    for column in range(1,6):
        print(row*column , end=" ")
    print()

#challenge
n=int(input("Enter a number :"))

for row in range(1,n+1):
    for column in range(1,row+1):
        print(column , end="")
    print()
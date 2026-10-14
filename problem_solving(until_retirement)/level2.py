#Q11
for i in range (1,11):
    print(i)

#Q12
n=int(input("Enter a number :"))
for i in range(1,n+1):
    print(i ,end=" ")
print()


#Q13
n=int(input("Enter a number :"))

for i in range (1,n+1):
    if i%2==0:
        print(i)

#Q14
n=int(input("Enter a number :"))

for i in range (1,n+1):
    if i%2!=0:
        print(i)

#Q15
n=int(input("Enter a nubmer :"))
sum=0
for i in range (1,n+1):
    sum=i+sum
print(sum ,end="")
print()

#Q16
n=int(input("Enter a number :"))
multiple=1

for i in range(1,n+1):
    multiple=multiple*i
print(multiple, end="")
print()

#Q17
m=int(input("Enter a number :"))

for i in range (1,11):
    print(m*i,end=" ")
print() 


#Q18
c=int(input("Enter a number :"))
count=0
for i in range(1,c+1):
    if i%3==0:
        count+=1
print(count)

#Q19
n=int(input("Ente a number :"))
m=1
for i in range(1,n+1):
    m=m*i
print(m,end=" ")
print()

#Q20
n=int(input("Enter a number :"))
t=1
for i in range (1,n+1):
    i=i*7
    print(i,end=" ")
print()
# Q1
a = 0
while a < 5:
    print("hello")
    a += 1


# Q2
i = 1
while i < 10:
    print(i)
    i += 1


# Q3
i = 1
while i < 10:
    print(i + 1)
    i += 1


# Q4
i = 10
while i > 0:
    print(i)
    i -= 1

# The reversed(range()) version is also simply:
i = 9
while i >= 1:
    print(i)
    i -= 1


# Q5
i = 5
while i <= 50:
    print(i)
    i += 5


# Q6
i = 2
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1


# Q7
i = 1
while i < 20:
    if i % 2 != 0:
        print(i)
    i += 1


# Q8
i = 1
while i < 20:
    if i % 3 == 0:
        print(i)
    i += 1


# Q9
i = 20
while i > 1:
    print(i)
    i -= 2


# Q10
num = int(input("Enter a number :"))

i = 0
while i < num:
    print(i + 1)
    i += 1


# Q11
n = int(input("Enter a number :"))

i = 1
while i < n:
    if i % 2 == 0:
        print(i)
    i += 1


# Q12
n = int(input("Enter a number :"))

i = 0
while i < n:
    if i % 2 != 0:
        print(i)
    i += 1


# Q13
n = int(input("Enter a number :"))

i = 1
while i < n:
    if i % 3 == 0:
        print(i)
    i += 1


# Q14
num = int(input("Enter a number :"))

i = 1
while i < num:
    if i % 2 == 0 and i % 3 == 0:
        print(i)
    i += 1


# Q15
nun = int(input("Enter a number :"))

i = 1
while i < nun:
    if i % 2 == 0:
        print(i)
    i += 1


# Q16
nn = int(input("Enter a number :"))

i = 1
while i <= nn:
    nn = nn + i
    i += 1

print(nn)


# Q17
n = int(input("Enter a number :"))
sum = 0

i = 1
while i <= n:
    if i % 2 == 0:
        sum = sum + i
    i += 1

print(sum)


# Q18
n = int(input("Enter a number :"))
sum = 0

i = 1
while i <= n:
    if i % 2 != 0:
        sum = sum + i
    i += 1

print(sum)


# Q19
muber = int(input("Enter a number :"))

i = 1
while i <= 10:
    print(muber * i)
    i += 1


# Q20
n = 1
number = int(input("Enter a number :"))

i = 1
while i <= number:
    n = n * i
    i += 1

print(n)


#Q1
i = 0
while i<5:
    print("Hello")
    i+=1


#Q2
i=1
while i < 11:
    print(i)
    i+=1


#Q3
i = 10
while i >0:
    print(i , end=" ")
    i-=1

#Q4
i = 0
while i<=20 :
    print(i)
    i+=2

#Q5
i = 1
while i <20:
    print(i)
    i+=2

#Q6
n=0

while i ==  0:
    i=int(input("Enter a number :"))
    print(i)
    i+=1
#Q1
for i in range(1, 8):
    if i == 5:
        break
    print(i)
print("Finished")

# 1, 2, 3, 4, 5 Finished


#Q2
word = "skyline"

for ch in word:
    if ch in "aeiou":
        break
    print(ch)
# k=skyl


#Q3
n = 2

while n <= 10:
    print(n)
    if n == 6:
        break
    n += 2

2, 4, 6

#Q4
limit = int(input("Enter a number :"))
for i in range (1,limit+1):
    if i == 7:
        break
    print(i , end=" ")


#Q5
word = input("Enter a word :")
target = "a"
for i in word:
    
    if i == target:
        break
    print(i , end = " ")


#Q6

numbers = input("Enter numbers separated by spaces: ").split()

for i in numbers:
    i = int(i)

    if i < 0:
        break

    print(i, end=" ")

# or

word = int(input("Enter a number: "))

for i in range(word):
    num = int(input("Enter a number: "))

    if num < 0:
        break

    print(num, end=" ")

#Q7
for row in range(1, 4):
    for col in range(1, 5):
        if col == 3:
            break
        print(row, col)

#11 12 21 22 31 32  

#Q8
character = input("Enter a word :")

for i in character:
    if i == "o":
        print("Found")
        break
    else:
        print("Not Found")

# or
str=input("ENter a stiring :").strip().lower()
flag=True

for ch in str:
    if ch == "o":
        flag=False
        print("Found")
if flag:
    print("Not Found")


#Q9
for i in range(1, 7):
    if i == 4:
        continue
    print(i)

#1,2,3,5,6,7


#Q10
for ch in "education":
    if ch in "aeiou":
        continue
    print(ch, end="")

# skips those

#Q11
n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)

# 1,2


#Q12
n = int(input("Enter a number :"))

for i in range(1, n +1 ):
    if i%3==0:
        continue
    print(i)


#Q13
sting = input("Enter a word :")
character = input("Enter character to be skipped :")

for i in sting:
    if i == character:
        continue
    print(i , end="")
print()


#Q14
marks =(input("Enter marks :")).split()

for i in marks:
    if int(i):

        if i < 40:
            continue
    print(i,end=" ")
print()

# or

n = int(input("How many marks do you want to enter? "))

for i in range(n):
    marks = int(input("Enter marks: "))

    if marks < 40:
        continue

    print(marks, end=" ")
print()


#Q15
for i in range(1, 5):
    if i == 2:
        continue
    print("A", i)
    print("B", i)

# A 1 , B 1 , A 3 , B 3 , A 4 , B 4


#Q16
n = 0

while n < 5:
    n+=1
    if n == 3:
        continue
    print(n)



#Q17
vowel = input("Enter a word :").lower()
count=0

for i in vowel:
    if i == "a" or i == "e" or i == "i" or i =="o" or i =="u":
        count+=1
print("There are " , count , "Vowel")


#Q18
for i in range(1, 4):
    print(i)
else:
    print("Done")

# 1,2,3 Done


#Q19
for i in range(1, 5):
    if i == 2:
        continue
    print(i)
else:
    print("Completed")

# 1,3,4 Completed

# #Q22
numbers = input("Enter number separated by spaces :").split()
target = int(input("Enter target :"))

for i in numbers:
    if int(i) == target:
        print("Found")
        break 
else:
    print("Not Found")


str=input("ENter a stiring :").strip().lower()
flag=True


# Q23
for ch in str:
    if ch == "o":
        flag=False
        print("Found")
if flag:
    print("Not Found")

#Q24
n = int(input("Enter a number :"))

for i in range (2,n):
    if i % i ==0 :
        print("Not Prime")
        break
else:
    print("Prime")




#Q25
# All are even

#Q26
# A
# 
# C

#Q27
fruit="banana"
count=0
for i in fruit:
    if i in "a":
        count+=1
        if count>=2:
            print("a")
            break
else:  
    print("no repeated character")          

#Q28
#1
#2
#3

#Q29
#Finished

#Q30
#Loop ended

#Q31
for i in range(1,6):
    if i%2==0:
        pass
    print(i)

#Q32
choice = input("Enter your choice: ")

if choice == '1':
    print("Dosa")
elif choice == '2':
    pass 
else:
    print("Invalid choice!")

print("Program closed")

#Q33 A
# 1
# 2
# 3
# 4

#Q33 B
# 1
# 2
# 4

#Q34
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#Q35
#1
#3

#Q36
x=[-2,4,7,9]
for i in x:
    if i<0:
        continue
    if i==7:
        print("Target Found")
        break
else:
    print("Target not found")    

#Q37
n=[2,0,4,-1,8]
for i in n:
    if i==0:
        continue
    if i== -1:
        break
    print(i)
else:
    print("All values processed")

#Q38
# 1 1
# 1 3
# Inner loop completed
# 2 1
# 2 3
# Inner loop completed

#Q39
num=[-3,8,12,24]
for i in num:
    if i<0:
        continue
    if i%4==0 and i%6==0:
        print("Found:",i)
        break
else:
    print("No matching number")  

#Q40
#1. break
#2. continue
#3. for-else
#4. pass
#5. continue
#6. break
#7. for-else
#8. pass
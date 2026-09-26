#Q1
for i in range(3):
    for j in range(3):
        print("*" , end =" ")
    print()

#Q2      
for i in range (1,4):                 # for i in range(3):                     #for i in range(3):
    for j in range(1,4):
        print(j, end=" ")                                                      #  for j in range(3):
    print()                           #     for j in range(1, 4):              #    print(j + 1, end=" ")
                                      #         print(j, end=" ")              #  print()
                                      #     print()

#Q3
for i in range(3):
    for j in range(3):
        print(i+1 , end=" ")
    print()


#Q4
for i in range(5):
    for j in range(i+1):
        print("*" , end=" ")
    print()

#Q5
for i in range(5,0,-1):
    for j in range (i):
        print("*" , end=" ")
    print()

#Q6
for i in range(5):
    for j in range(i+1):
        print(j+1 , end=" ")
    print()

#Q7
for i in range(1,6):
    for j in range(i):
        print(i, end=" ")
    print()

#Q8
for i in range(1,11):
    for j in range(1,6):
        print(j, "*" , i ,"=" , i*j  ,end="       ")
    print()

#Q9
for i in range(1,4):
    for j in range(1,6):
        print(i*j, end=" ")
    print()

#Q10
for i in range(1,6):
    for j in range(1,6):
        print(j**2 , end=" ")
    print()

#Q11*
n="ABCDE"
for i in range(1,6):
    for j in range(i):
        print(n[j],end=" ")
    print()

for i in range(5):
    alpha=""
    for j in range(0, i+1):
        alpha+=chr(65+j)+ " "
    print(alpha)


#Q12
for i in range(5):
    alpha=""
    for j in range (0, i+1):
        alpha+=chr(65+i) + " "
    print(alpha)

#Q13
for i in range(1,10,2):
    for j in range(1, i+1 ,2):
        print(j,end=" ")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(2 * j - 1, end=" ")
    print()

#or
n = int(input("Enter a number :"))
for i in range (n+1):
    for j in range(2*i+2):
        if j%2!=0:
            print(j , end=" ")
    print()
    

#Q14
for i in range(2,11,2):
    for j in range(2,i+1 ,2):
        print(j, end=" ")
    print()

#Q15
for i in range(5):
    for j in range(5):
        print("*" , end=" ")
    print()

#Q16
for i in range(5):
    for j in range(1,6):
        print(j, end=" ")
    print()

#Q17
num=1

for i in range (3):
    for j in range(3):
        print(num , end=" ")
        num+=1
    print()

num = 1

for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

#Q18
no=1

for i in range(4):
    for j in range(5):
        print(no, end=" ")
        no+=1
    print()

#Q19
for i in range(1,4):
    for j in range(1,4):
        print(f"{(i,j)}" , end=" ")
    print()

for i in range(1,4):
    for j in range(1,4):
        print((i,j) , end=" ")
    print()

#Q20
for i in range(1,4):
    for j in range(1,4):
        print(i,j)

#Q21
for i in range(11):
    for j in range(1,11):
        print(i*j , end=" ")
    print()

#Q22
for i in range(6):
    for j in range(i):
        print(i, end="")
    print()

#Q23
for i in range (6,0,-1):
    for j in range(i):
        print(j,end="")
    print()

for i in range (6,0,-1):
    for j in range(1,i):
        print(j,end="")
    print()

#Q24
for i in range(5,0,-1):
    for j in range(5,5-i,-1):
        print(j,end="")
    print()

#Q25
for i in range(5):
    for j in range(5):
        print(i+1 , end="")
    print()

for i in range(3,0,-1):
    for j in range(3,0,-1):
        print(j , end=" ")
    print()
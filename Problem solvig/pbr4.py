# #Q1
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)


# #Q2
# for i in range(1,4):
#     for j in range(i,4):
#         print( i , f"x" , j ,"=" , i*j)


# #Q3
# for i in range(3):
#     for j in range(4):
#         print("*" ,end="")
#     print()


# #Q4
# for row in range(2):
#     for col in range(3):
#         print(f"({row},{col})" , end=" ")
#     print()



# #Q5
# n=int(input("Enter a number :"))

# for i in range(1,n+1):
#     for j in range(n):
#         print(i , end="")
#     print()



# #Q6
# N = int(input("Enter a number :"))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         print(j,end="")
#     print()



# #Q7
# input = int(input("Enter a number :"))

# for i in range(1,input+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


#Q8
n = int(input("Enter a number :"))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j , end="")
    print()
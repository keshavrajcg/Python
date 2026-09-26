# #Q1
# data=(input("enter characters: "))

# uppercase=0
# lowercase=0
# digits=0
# spaces=0
# special_characters=0


# for i in data:
#     if i>="A" and i<="Z":
#         uppercase+=1
#     elif i>="a" and i<="z":
#         lowercase+=1
#     elif i>="0" and i<="9":
#         digits+=1
#     elif i==" ":
#         spaces+=1
#     else:
#         special_characters+=1



# print("number of uppercase letters :",uppercase)
# print("number of lowercase letters :", lowercase)
# print("number of digits :" ,digits)
# print("number of spaces : ",spaces)
# print("number of special characters :",special_characters)


# if uppercase>lowercase and uppercase>digits and uppercase>spaces and uppercase>special_characters:
#     print("uppercase letters has the highest count")
# elif lowercase>uppercase and lowercase>digits and lowercase>spaces and lowercase>special_characters:
#     print("lowercase letters has the highest count")
# elif digits>uppercase and digits>lowercase and digits>spaces and digits>special_characters:
#     print("digits has the highest count")
# elif spaces>uppercase and spaces>lowercase and spaces>digits and spaces>special_characters:
#     print("spaces has the highest count")
# elif special_characters>uppercase and special_characters>lowercase and special_characters>digits and special_characters>spaces:
#     print("special characters has the highest count")
# else:
#     print("Tie")



# #Q3
# sentence=input("Enter a sentence :")
# words=sentence.split()

# highest_score=0
# highest_word=""

# for i in words:
#     score=0
#     for letter in words:
#         if letter in "aeiouAEIOU":
#             score+=2
#         elif letter >="0" and letter <="9":
#             score+=3
#         elif letter >="a" and letter <= "z" or letter >= "A" and letter <= "Z":
#             score+=1
#         else:
#             score+=4
#     print(i, score)

#     if score>highest_score:
#         highest_score=score
#         highest_word=i
# print("Highest score :" , highest_word)
# print("Score :" , highest_score)

# # sentence = input("Enter a sentence: ")

# # words = sentence.split()

# # highest_score = 0
# # highest_word = ""

# # for word in words:
# #     score = 0

# #     for letter in word:
# #         if letter in "aeiouAEIOU":
# #             score += 2
# #         elif letter >= "0" and letter <= "9":
# #             score += 3
# #         elif letter >= "a" and letter <= "z" or letter >= "A" and letter <= "Z":
# #             score += 1
# #         else:
# #             score += 4

# #     print(word, score)

# #     if score > highest_score:
# #         highest_score = score
# #         highest_word = word

# # print("Highest:", highest_word)
# # print("Score:", highest_score)

# #Q2
# excellent=0
# good=0
# passed=0
# fail=0

# for i in range(10):
#     marks=int(input("Enter a number :"))

#     if marks>=75 and marks<=100:
#         print("Excellent")
#         excellent+=1
#     elif marks>=50 and marks<75:
#         print("Good")
#         good+=1
#     elif marks>=35 and marks<35:
#         print("Pass")
#         passed+=1
#     elif marks>=0 and marks<=34:
#         print("Fail")
#         fail+=1
#     else:
#         print("Invalid input")

# print("Excellent students" , excellent)
# print("Good students" , good)
# print("Passed students" , passed)
# print("Failed students" , fail)

# #Q4
# for i in range(5):
#     passkey=input("Enter password :")
#     count=0

#     upper=0
#     lower=0
#     digit=0
#     special=0

#     if len(passkey)>=8:
#         count+=1

#     for chr in passkey:
#         if chr>="A" and chr<="Z":
#             upper=1
#         elif chr>="a" and chr<="z":
#             lower =1
#         elif chr>="0" and chr<="9":
#             digit=1
#         else:
#             special=1
# count+=upper+lower+digit+special

# if count == 5:
#             print("Strong")
# elif count >= 3:
#             print("Medium")
# else:
#             print("Weak")

# #Q5
# sentence=input("enter sentence: ").split()
# for i in sentence:
#     if len(i)<=3:
#         print(f"word:{i} length: Short")
#     elif len(i)>=4 and len(i)<=6:
#         print(f"word:{i} length: Medium")
#     else:
#         print(f"word:{i} length: Long")

# #Q6
# even=0
# odd=0

# for i in range(5):
#     no=input("Enter a word")
#     for i in no:
#         print(i)
#         if len(i)%2==0:
#             print("Even words")
#             even+=1
#         else:
#             print("Odd words")
#             odd +=1

# if even>odd:
#     print("Even words are more")
# elif odd>even:
#     print("Odd words are more")
# else:
#     print("Odd and even are equal")

# #Q7
# word = input("Enter sentence: ")

# for i in word:
#      cnt=0

#      for j in word:
#           if i==j:
#                cnt+=1
#      if cnt>1:
#           if count ==2:
#                print(i,"=>",cnt,"Duplicate")
#           elif count<=4:
#                print(i,"=>" , count, "Repeated")
#           else:
#              print(i, "=>", cnt , "Highly Repeated")

# #Q8
# luxury=0
# premium=0
# regular=0
# budget=0
# total=0

# for i in range(8):
#     product=int(input("Enter product prices :"))

#     total += product

#     if product>=5000:
#           print("Luxury")
#           luxury+=1
#     elif product>=2000:
#           print("Premium")
#           premium+=1
#     elif product>=500:
#           print("Regular")
#           regular+=1
#     elif product>0 and product<500:
#           print("Budget")
#           budget+=1
#     else:
#           print("Invalid Data")

# average=total/8

# print("Luxury :" , luxury )
# print("Premium :" , premium)
# print("Regular :" , regular)
# print("Budget :" , budget)
# print("Total :", total)
# print("Average :", average)

# #Q9

# position=0
# even_position=0
# odd_position=0
# vowel=0
# consonant=0
# digit=0
# special_character=0

# word = input("Enter sentence: ")

# for i in word:
#      print("Character:" , i)
#      position+=1
#      if position%2==0:
#           print("Even positon")
#           even_position+=1
#      else:
#           print("Odd position")
#           odd_position+=1
#      if i.isalpha():
#           if i.lower() in "aeiou":
#                print("Vowel")
#           else:
#                print("Consonant")
#                consonant+=1
#      elif i.isdigit():
#           print("Digit")
#           digit+=1
#      else:
#           print("Special character")
#           special_characters+=1
#      print()

# print("Even positon characters:", even_position)
# print("Odd position characters:" , odd_position)
# print("Vowels:",vowel)
# print("Consonants:" , consonant)
# print("Digits:",digit)
# print("Speical characters:" , special_characters)

# #Q10


# #Q11
# for i in range(5):
#     user_name=input("Enter username :")

#     lenght=0
#     first_chr=0
#     digits=0
#     underscores=0
#     invd_special_characters=0

#     if user_name[0].isalpha():
#          first_chr = True
#     else:
#          first_chr = False

#     for j in user_name:
#          if j.isdigit():
#               digit+=1
#          elif j == "_":
#               underscores+=1
#          else:
#               print("Invalid")

# # #Q12
# # sentences=input("Enter a sentence :")
# # vowels=0
# # consonants=0
# # for i in sentences:
# #      if i.lower() in "aeiou":
# #           vowels+=1
# #      elif i.isalpha():
# #           consonants+=1

# # Q12
# sentences = input("Enter a sentence: ")

# vowels = 0
# consonants = 0

# a = 0
# e = 0
# i_count = 0
# o = 0
# u = 0

# for i in sentences:

#     if i.lower() in "aeiou":
#         vowels += 1

#         if i.lower() == "a":
#             a += 1
#         elif i.lower() == "e":
#             e += 1
#         elif i.lower() == "i":
#             i_count += 1
#         elif i.lower() == "o":
#             o += 1
#         elif i.lower() == "u":
#             u += 1

#     elif i.isalpha():
#         consonants += 1

# if vowels > consonants:
#     print("Vowels Win")

# elif consonants > vowels:
#     print("Consonants Win")

# else:
#     print("Draw")

# print("Vowels:", vowels)
# print("Consonants:", consonants)

# print("Frequency of a:", a)
# print("Frequency of e:", e)
# print("Frequency of i:", i_count)
# print("Frequency of o:", o)
# print("Frequency of u:", u)

# #Q2

# Excellent=0
# Good=0
# Pass=0
# Fail=0

# for i in range(10):
#     n=int(input("Enter mark's of sutdents :"))
#     if n >=75 and n <=100:
#         print("Exellent")
#         Excellent+=1
#     elif n >=50 and n<75 :
#         print("Good")
#         Good+=1
#     elif n >= 35 and n<50:
#         print("Pass")
#         Pass+=1
#     elif n>=0 and n<35:
#         print("Fail")
#         Fail+=1
#     else:
#         print("Invalid")

# print("Total Excellent :" , Excellent)
# print("Total Good :" , Good )
# print("Total Passed :" , Pass)
# print("Total Failed :" , Fail)

#Q1
Vowel=0
Consonant=0
Digit=0
Speicalchr=0

m=input("Enter strings")

if m =="aeiouAEIOU":
    Vowel+=2
    if m >="A" or m <="Z" or m>="a" or m<="z":
        Consonant+=1
    if m>=0 and m <=9:
        Digit+=3
    else:
        Speicalchr+=4
print(Vowel, Consonant, Digit, Speicalchr)

#Q4


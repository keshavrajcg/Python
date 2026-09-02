#Q1
name="Keshav"
city="Samastipur"
fav_p_lang="c++"
message='This is about me!!'
print(name)
print(city)
print(fav_p_lang)
print(message)

#Q2
a=""
print(a)
print(len(a))
print(type(a))

#Q3
b="Python Programming"
print(b[:])
print(len(b))
print(b[0])
print(b[-1])
print(b[2])
print([17])

#Q4
c="Programming"
print(c[0])
print(c[1])
print(c[4])
print(c[10])

#Q5
print(c[-1])
print(c[-2])
print(c[-3])
print(c[-11])

#Q6
my_name="Keshav Singhania"
print(my_name[0])
print(my_name[-1])
print(my_name[7])

#Q7
d="Python Programming"
print(d[0:7])
print(d[8:])
print(d[:])
print(d[-5:])

#Q8
e="ABCDEFGHIJKL"
print(e[ : : 2])
print(e[::3])
print(e[1:8:2])
print(e[::-1])

#9
print(d[-5:])
print(d[-10:])
print(d[::-1])

#Q10
f="Rakshbandhan"
print(f[:3])
print(f[-3:])
print(f[::2])
print(f[::-1])
print(f[1:-1])

#Q11
g="Treats"
h="Treatsaregood"
i="Treat is nice"
print(len(g),len(h),len(i))

#Q12
print(len(d))

#Q13
first_name="Keshav"
last_name="Singhania"
print(first_name+" "+last_name)

#Q14
name="Raju"
age="5"
city="Dholakpur"
lang="Css"
print(name+" is "+age+" years old " +" Lives in " + city + " Loves " +lang)

#Q15
a="bana"
b=2
c=str(b)
print(a+c)

#Q16
t="@"
print(t*3)
print(t*5)
print(t*10)

#Q17
r="*"
print(r*10)

#Q18
a="python programming language"
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.swapcase())

#Q19
a="Python"
b="python"
print(a==b)
c=a.lower()
d=b.lower()
print(c==d)

#Q20
q="Python is a programming language"
print("Python" in q)
print("programming" in q)
print("Java" in q)
print("language" in q)

#Q21
print(q.find("Python"))
print(q.find("programming"))
print(q.find("language"))
print(q.find("Java"))

#Q22
print(q.index("Python"))
print(q.index("Java"))

#Q23
a="banana"
print(a.count("a"))
print(a.count("n"))
print(a.count("b"))

#Q24
filename="student_notes.pdf"
print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))

#Q25
text="I am learning Java"
print(text.replace("Java","Python"))

#Q26
text="apple apple apple"
print(text.replace("apple","mango",3))

#27
print(text.replace("apple","mango",2))

#Q28
text="Python"
text.upper()
print(text)

#Q29
text=" Python programming "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

#Q30
name=" King "
print(name.strip())

#Q31
a="Python is easy to learn"
print(a.split())

#Q32
a="apple,banana,mango,orange"
print(a.split(","))

#Q33
word=["Python","is","easy"]
print(" ".join(word))

#Q34
a="Python-is-easy"
print("/".join(a.split("-")))

#Q35
name="Raunak"
age=20
city="Mastipur"
print(f"Name: {name}, Age: {age}, City: {city}")

#Q36
a=10
b=20
print(f"Sum of {a} and {b} is {a+b}")

#Q37
text="Python"
print(text[20]) #IndexError: string index out of range
text[0]= "J"
print(text) #TypeError: 'str' object does not support item assignment
age=20
print("Age: "+age) #TypeError: can only concatenate str (not "int") to str
text="Python"
print(text.index("Java")) #ValueError: substring not found

#correct form
text = "Python"
print(text[0])

text = "Python"
text = "J" + text[1:]
print(text)

age = 20
print("Age: " + str(age))

text = "Python"

if "Java" in text:
    print(text.index("Java"))
else:
    print("Java not found")

#Q38
name = "Roland"

print("Original:", name)
name = name.strip()
print("Cleaned:", name)
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title case:", name.title())
print("Length:", len(name))
print("First character:", name[0])
print("Last character:", name[-1])

#Q39
sentence = "Lorem ipsum dolor sit amet"

print("Original sentence:", sentence)

print("Number of characters:", len(sentence))
print("Number of words:", len(sentence.split()))
print("First character:", sentence[0])
print("Last character:", sentence[-1])
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())
print("Contains Python:", "Python" in sentence)


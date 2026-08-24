#Q24
student_name="Rohit"
student_age=20
student_height=6.0
student=True
student_result=None

print(type(student_name))
print(type(student_age))
print(type(student_height))
print(type(student))
print(type(student_result))

#Q25
a=50
b=50.0
c="50"

print(type(a))
print(type(b))
print(type(c))

#Q26
a=True
b="True"

print(type(a))
print(type(b)) #There types differ because one of the value useses colon("") which will be considered as a string value

#Q27
a=None
b="None"

print(type(a))
print(type(b)) #They differ because of the same concept the value "None" is considered as a string value 

#Q28
value=100
print(type(value))
value="101"
print(type(value)) #Data types changed as we used colons("") to reassign our value

#Q29
product_name="Mitacha"
product_quantity=90
product_price=999.9
availablity=True
product_discount=None

print(type(product_name), type(product_quantity), type(product_price), type(availablity), type(product_discount))

#Q30
model=10
speed=10.0
top="10"
winner=True
Podiums="True"
Losses=None
Damage="None"

print(type(model)) #int. It contains whole numbers and negative values also.
print(type(speed)) #float. It contains decimal values.
print(type(top)) #String. It contains colons "".
print(type(winner)) #Bool. It contains yes or no value.
print(type(Podiums)) #Str.
print(type(Losses)) #None-type. It shows empty value.
print(type(Damage)) #Str.
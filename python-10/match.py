# # # # # #Q1
# # # #  # i = int(input("Press 1 for pizza \n 2 for burger \n 3 for pasta\n 4 for sandwich:"))

# # # # # match i:
# # # # #     case 1 :
# # # # #         print("Pizza is selected")
# # # # #     case 2 :
# # # # #         print("Burger is selected")
# # # # #     case 3:
# # # # #         print("Pasta is selected")
# # # # #     case 4:
# # # # #         print("Sandwwich is selected")
# # # # #     case _:
# # # # #         print("Invalid menue choice")


# # # # # #Q2
# # # # # m = int(input("Enter your a choice from 1 to 5 :"))

# # # # # match m:
# # # # #     case 1:
# # # # #         print("Wi-Fi is selected")
# # # # #     case 2:
# # # # #         print("Bluetooth is selected")
# # # # #     case 3:
# # # # #         print("Mobile Data is selected")
# # # # #     case 4:
# # # # #         print("Airplane mode is selected")
# # # # #     case 5:
# # # # #         print("Exited")
# # # # #     case _:
# # # # #         print("Invalid Setting")


# # # # # #Q3
# # # # # b= int(input("Enter 1 to select Balance \n 2 to select Withdrawal \n 3 to Deposite \n 4 to Change pin \n 5 to Exit :"))

# # # # # match b:
# # # # #     case 1:
# # # # #         print("Check balance is selected")
# # # # #     case 2:
# # # # #         print("Withdraw money is selected")
# # # # #     case 3:
# # # # #         print("Deposite money is selected")
# # # # #     case 4:
# # # # #         print("Change PIN is selected")
# # # # #     case 5:
# # # # #         print("Exited")
# # # # #     case _:
# # # # #         print("Invalid input")


# # # # #Q4
# # # # t=input("Select signal color \nRed , Yellow , Green :").lower()

# # # # match t:
# # # #     case "red":
# # # #         print("Stop")
# # # #     case "yellow":
# # # #         print("Wait")
# # # #     case "green":
# # # #         print("Go")
# # # #     case _:
# # # #         print("Invalid signal")


# # # # #Q5
# # # # student=int(input("Enter your desired input from 1 to 5 :"))

# # # # match student:
# # # #     case 1 :
# # # #         print("View profile")
# # # #     case 2:
# # # #         print("View course")
# # # #     case 3:
# # # #         print("View attendance ")
# # # #     case 4:
# # # #         print("View marks")
# # # #     case 5:
# # # #         print("Logout")
# # # #     case _:
# # # #         print("Invalid input")


# # # #Q6
# # # shopping=int(input("Enter your opition \n1 for Electorinic \n2 for Clothing \n3 for Books \n4 for Grocery \n5 to Exit :"))

# # # match shopping:
# # #     case 1:
# # #         print("Opening Electorincs")
# # #     case 2:
# # #         print("Opening Clothing")
# # #     case 3:
# # #         print("Opening Books")
# # #     case 4:
# # #         print("Opening Grocery")
# # #     case 5:
# # #         print("Exiting")
# # #     case _:
# # #         print("Invalid input")


# # # #Q7
# # # services=int(input("Enter service :"))

# # # match services:
# # #     case 1:
# # #         print("Opening Account Balance")
# # #     case 2:
# # #         print("Opening Mini Statement")
# # #     case 3:
# # #         print("Opening Fund Transfer")
# # #     case 4:
# # #         print("Opening Bill payment")
# # #     case 5:
# # #         print("Opening Coustomer Support")
# # #     case _:
# # #         print("Invalid input")


# # # #Q8
# # # booking=int(input("Select time period"))

# # # match booking:
# # #     case 1:
# # #         print("Morning show selectec")
# # #     case 2:
# # #         print("Afternoon show selected")
# # #     case 3:
# # #         print("Evening show selected")
# # #     case 4:
# # #         print("Night show selected")
# # #     case _:
# # #         print("Invalid input")


# # # #Q9
# # # weather=input("Enter weather status \nSunny, Rainy, Cloudy, Snowy :").lower()

# # # match weather:
# # #     case "sunny":
# # #         print("Wear sunglasses")
# # #     case "rainy":
# # #         print("Carry an umbrella")
# # #     case "cloudy":
# # #         print("Weather may change")
# # #     case "snowy":
# # #         print("Wear warm clothes")
# # #     case _:
# # #         print("Invalid input")


# # # #Q10
# # # payment_mode=input("Enter payment mode \nUpi \nCard \nCash \nWallet :").lower()

# # # match payment_mode:
# # #     case "upi":
# # #         print("UPI Payment Selected")
# # #     case "card":
# # #         print("Card Payment Selected")
# # #     case "wallet":
# # #         print("wallet Payment Selected")
# # #     case "cash":
# # #         print("Cash Payment Selected")
# # #     case _:
# # #         print("Invalid input")


# # # #Q11
# # # file=input("Enter file extension name: ").lower()

# # # match file:
# # #     case "pdf":
# # #         print("Document")
# # #     case "jpg":
# # #         print("Image")
# # #     case "png":
# # #         print("Image")
# # #     case "mp3":
# # #         print("Audio")
# # #     case "mp4":
# # #         print("Video")
# # #     case _:
# # #         print("Unknown File Type")


# # # #Q12
# # # User = input("Enter user role \n Admin , Teacher , Student , Guest :").lower()

# # # match User:
# # #     case "admin":
# # #         print("Full Access")
# # #     case "teacher":
# # #         print("Teacher Dashboard")
# # #     case "student":
# # #         print("Student Dashboard")
# # #     case "guest":
# # #         print("Limited Access")
# # #     case _:
# # #         print("Invalid Role")


# # # #Q13
# # # day=int(input('''1 → Monday
# # # 2 → Tuesday
# # # 3 → Wednesday
# # # 4 → Thursday
# # # 5 → Friday
# # # 6 → Saturday
# # # 7 → Sunday \n
# # # Enter a day number \n '''))
# # # match day:
# # #     case 1 | 2 | 3 | 4 | 5 :
# # #         print("Weekday")
# # #     case 6|7:
# # #         print("Weekend")
# # #     case _:
# # #         print("Invalid day number")


# # # #Q14
# # # Priority=int(input("Enter priority number from 1 to 4 :"))

# # # match Priority:
# # #     case 1|2:
# # #         print("Normal Priority")
# # #     case 3|4:
# # #         print("Urgent Priority")
# # #     case _:
# # #         print("Invalid input")

# # # #Q15
# # # membership = int(input("Enter level from 1 to 4"))

# # # match membership:
# # #     case 1 | 2:
# # #         print("Basi Memebership")
# # #     case 3 | 4:
# # #         print("Premium Membership")


# # # #Q16
# # # user = input('''1 → Student
# # # 2 → Teacher''').lower()
# # # ent=int(input('''1 → View Courses
# # # 2 → View Marks
# # # 3 → View Attendance \n 
# # # Enter what you want to view from 1 to 3 :'''))
# # # match user:
# # #     case "student":
# # #         match ent:
# # #             case 1:
# # #                 print("View Courses")
# # #             case 2:
# # #                 print("View Marks")
# # #             case 3:
# # #                 print("View Attendance")
# # #             case _:
# # #                 print("Invalid input")

# # #     case "teacher":
# # #         match ent:
# # #             case 1:
# # #                 print("View Students")
# # #             case 2:
# # #                 print("Enter Marks")
# # #             case 3:
# # #                 print("View Attendance")
# # #             case _:
# # #                 print("Invalid Input")
# # #     case _:
# # #         print("Invalid")



# # # #Q17
# # # account = int(input('''1 → Savings
# # # 2 → Current : '''))

# # # work = int(input('''1 → Check Balance
# # # 2 → Deposit
# # # 3 → Withdraw : '''))

# # # match account:
# # #     case 1:
# # #         print("Savings Account")
# # #         match work:
# # #             case 1:
# # #                 print("Check Balance Selected")
# # #             case 2:
# # #                 print("Deposit Selected")
# # #             case 3:
# # #                 print("Withdraw Selected")
# # #             case _:
# # #                 print("Invalid input")
# # #     case 2:
# # #         print("Current Account")
# # #         match work:
# # #             case 1:
# # #                 print("Check Balance Selected")
# # #             case 2:
# # #                 print("Deposit Selected")
# # #             case 3:
# # #                 print("Withdraw Selected")
# # #             case _:
# # #                 print("Invalid input")
# # #     case _:
# # #         print("Invalid input")


# # # #Q18
# # # category = int(input('''1 → Electronics
# # # 2 → Clothing : '''))


# # # match category:
# # #     case 1:
# # #         electronics = int(input('''1 → Mobile
# # # 2 → Laptop
# # # 3 → Headphones : '''))

# # #         match electronics:
# # #             case 1:
# # #                 print("Mobile Selected")
# # #             case 2:
# # #                 print("Laptop Selected")
# # #             case 3:
# # #                 print("Headphones Selected")
# # #             case _:
# # #                 print("Invalid input")
# # #     case 2:
# # #         clothing=int(input('''1 → Shirt
# # # 2 → Jeans
# # # 3 → Shoes'''))
# # #         match clothing:
# # #             case 1:
# # #                 print("Shirt Selected")
# # #             case 2:
# # #                 print("Jeans Selected")
# # #             case 3:
# # #                 print("Shoes Selected")
# # #             case _:
# # #                 print("Invalid input")

# # #     case _:
# # #         print("Invalid input")


# # #Q19
# # select = int(input("press 1 for Vegetarian ; press 2 for Non-Vegetarian"))

# # match select:
# #     case 1:
# #         food = int(input("""Select dish \n 1 → Paneer
# #                             2 → Dal
# #                             3 → Veg Biryani : """))
# #         match food :
# #             case 1 :
# #                 print("Paneer Selected")

# #             case 2:
# #                 print("Dal Selected")
# #             case 3:
# #                 print("Veg Biryani Selected")
# #             case _:
# #                 print("Invalid input")

# #     case 2:
# #         food = int(input('''Select dish \n 1 → Chicken Biryani
# # 2 → Chicken Curry
# # 3 → Fish Fry :'''))    
# #         match food:
# #             case 1:
# #                 print("Chicken Biryani Selected")
# #             case 2:
# #                 print("Chicken Curry Selected")
# #             case 3:
# #                 print("Fish Fry Selected")
# #     case _:
# #         print("Invalid input")


# # #Q20
# # first_number=int(input("Enter a number :"))
# # second_number=int(input("Enter second number :"))
# # operator=input("Enter operator + , - , * , / :")

# # match operator:
# #     case "+":
# #         print("Result = " , first_number+second_number)
# #     case "-":
# #         print("Result = " ,first_number - second_number)
# #     case "*":
# #         print("Result =" ,first_number * second_number)
# #     case "/":
# #         print("Result =" ,first_number / second_number)
# #     case _:
# #         print("Invalid input")


# # #Q21
# # choice = int(input('''1 → Celsius to Fahrenheit
# # 2 → Fahrenheit to Celsius :'''))

# # temp = int(input("Enter temperature"))

# # match choice:
# #     case 1:
# #         result= ((temp*9)/5)+32
# #         print("Temperature" , result , "F")
# #     case 2:
# #         result = ((temp-32)*5)/9
# #         print(f"Temperature : {result} C")
# #     case _:
# #         print("Invalid iput")


# # #Q22
# # unit = int(input(''' Enter what you want to convert to \n 1 → Kilometers to Meters
# # 2 → Meters to Kilometers
# # 3 → Kilograms to Grams
# # 4 → Grams to Kilograms : '''))
# # value =int(input("Enter value :"))

# # match unit :
# #     case 1:
# #         print(value *1000 , "meters")
# #     case 2:
# #         print(value / 1000 , "kilometers")
# #     case 3:
# #         print(value * 1000 , "grams")
# #     case 4:
# #         print(value / 1000 , "kilograms")
# #     case _:
# #         print("Invalid input")



# #Q23
# account = int(input ( '''1 → Savings
# 2 → Current : '''))
# amount= int(input("Enter amount :"))

# match account :
#     case 1:
#         print("Savings Account")
#         if amount>0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid")
#     case 2:
#         print("Current Account")
#         if amount>0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid")


# #Q24
# menu = int(input('''1 → Start Exam
# 2 → View Result
# 3 → Exit : '''))

# match menu:
#     case 1:
#         age = int(input("Enter your age :"))
#         if age >=18:
#             print("You can start your exam")
#         else:
#             print("Not applicable")
#     case 2:
#         print("Result awaited")
#     case 3:
#         print("Exited")


#Q25
ticket = int(input('''1 → Regular
2 → Premium
3 → VIP : '''))

match ticket:
    case 1|2|3:
        age = int(input("Enter your age :"))
        if age >=0 and age <5:
            print("Entery is free")
        else :
            match ticket:
                case 1:
                    print("Regular Selected")
                case 2:
                    print("Premium Selected")
                case 3:
                    print("VIP Selected")
                case _:
                    print("Invalid input")

    case _:
        print("Invalid input")


#Q26
device = int(input(''' Enter Device \n 1 → Light
2 → Fan
3 → AC
4 → TV : '''))

match device:
    case 1:
        print("Light Controller Opened")
    case 2:
        print("Fan Controller Opened")
    case 3:
        print("AC Controller Opened")
    case 4:
        print("TV Controller Opened")
    case _:
        print("Invalid input")


#Q27
department = int(input('''Enter Department \n 1 → General Medicine
2 → Cardiology
3 → Orthopedics
4 → Pediatrics
5 → Emergency : '''))

match department:
    case 1:
        print("General Medicine Selected")
    case 2:
        print("Cardiology Selected")
    case 3:
        print("Orthopedics Selected")
    case 4:
        print("Pediatrics Selected")
    case 5:
        print("Emergency Selected")
    case _:
        print("Invalid Department")


#Q28
railway_ticket=int(input('''1 → Book Ticket
2 → Cancel Ticket
3 → Check PNR
4 → Train Schedule
5 → Exit : '''))

match railway_ticket:
    case 1:
        print("Booking in progress")
    case 2:
        print("Canceling ticket")
    case 3:
        print("Checking PNR")
    case 4:
        print("Checking Train schedule")
    case 5:
        print("Exited")
    case _:
        print("Invalid input")



#Q29
library = int(input('''Entere action \n 1 → Search Book
2 → Issue Book
3 → Return Book
4 → View Issued Books
5 → Exit : '''))

match library:
    case 1:
        print("Searching Book")
    case 2:
        print("Issuing Book")
    case 3:
        print("Returning Book")
    case 4:
        print("History Loading")
    case 5:
        print("Exiting")
    case _:
        print("Invalid input")


#Q30
status = input('''Enter status \n
placed
confirmed
preparing
out_for_delivery
delivered
cancelled : ''').lower()

match status:
    case "placed":
        print("Your order is placed")
    case "confirmed":
        print("Your order is confirmed")
    case "preparing":
        print("Your order is being prepaired")
    case "out_for_delivery":
        print("Your order is on the way")
    case "deliverd":
        print("Your order is deliverd")
    case "cancelled":
        print("Your order is cancelled")
    case _:
        print("Invalid input")


#Q31
banking = int(input('''Enter your banking type \n 
1 → Personal Banking
2 → Business Banking : '''))

match banking:
    case 1:
        action=int(input('''1 → Balance
2 → Transfer
3 → Loan'''))
        match action:
            case 1:
                print("Personal Balance Selected")
            case 2:
                print("Personal Transfer Selected")
            case 3:
                print("Personal Loand Selected")
            case _:
                print("Invalid input")
    case 2:
        action=int(input('''1 → Balance
2 → Payroll
3 → Business Loan'''))
        match action:
            case 1:
                print("Business Balance Selected")
            case 2:
                print("Business Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid input")
    case _:
        print("Input Invalid")




#Q32
user = int(input('''Enter User type \n 1 → Student
2 → Teacher
3 → Parent : '''))

match user:
    case 1 :
        select = int(input('''Enter Action \n 1 → Student
2 → Teacher
3 → Parent : '''))
        match select:
            case 1:
                print("Viewing Marks")
            case 2:
                print("Viewing Attendance")
            case 3:
                print("Viewing Homeworkd")
            case _:
                print("Invalid input")
    case 2:
        select=int(input('''Enter Action \n 1 → Enter Marks
2 → Attendance
3 → Assign Homework : '''))

        match select:
            case 1:
                print("Entering Marks")
            case 2:
                print("Enter Attendance")
            case 3:
                print("Assigning Homework")
            case _:
                print("Invalid input")
    case 3:
        select=int(input('''Enter Action \n
        1 → Child Marks
2 → Child Attendance
3 → Contact Teacher'''))            
        match select:
            case 1:
                print("Viewing Child's Marks")
            case 2:
                print("Viewing Child's Attendance")
            case 3:
                print("Viewing Teacher's Contact")
            case _:
                print("Invalid input")
    case _:
        print("Invalid input")



#Q33
transport=int(input('''Enter your transport mode \n1 → Flight
2 → Train
3 → Bus'''))

match transport:
    case 1:
        select = int(input('''1 → Economy
2 → Business : '''))

        match select:
            case 1:
                print("Economy Seat Selected")
            case 2:
                print("Business Seat Selected")
            case _:
                print("Invalid input")

    case 2:
        select = int(input('''1 → Sleeper
2 → AC'''))
        match select:
            case 1:
                print("Sleeper Seat Selecetd")
            case 2:
                print("AC Seat Selected")
            case _:
                print("Invalid input")
    case 3:
        select = int(input('''1 → Ordinary
2 → Volvo'''))
        match select:
            case 1:
                print("Odinary Bus Selected")
            case 2:
                print("Volvo Bus Selected")

            case _:
                print("Invalid input")

    case _:
        print("Invalid Input")


#Q34
console_menu = int(input('''Enter Action \n 1 → Start Game
2 → Load Game
3 → Settings
4 → Exit :'''))

match console_menu:
    case 1:
        print("Starting Game")
    case 2:
        print("Loading Game")
    case 3:
        setting=int(input('''1 → Sound
2 → Graphics
3 → Controls'''))
        match setting:
            case 1:
                print("Opening Sound Setting")
            case 2:
                print("Opening Graphics Setting")
            case 3:
                print("Opening Controls Setting")
            case _:
                print("Invalid input")
    case 4:
        print("Exited")
    case _:
        print("Invalid input")


#Q35
menu=int(input('''Select menu item \n 
1 → Starters
2 → Main Course
3 → Desserts
4 → Drinks '''))

match menu:
    case 1:
        display = int(input('''1 → Soup
2 → Spring Roll
3 → Garlic Bread '''))
        match display:
            case 1:
                print("Ordering Soup")
            case 2:
                print("Ordering Spring Roll")
            case 3:
                print("Ordering Garlic Bread")
            case _:
                print("Invalid input")
    case 2:
        display=int(input('''1 → Pizza
2 → Pasta
3 → Biryani'''))
        match display:
            case 1:
                print("Ordering Pizza")
            case 2:
                print("Ordering Pasta")
            case 3:
                print("Ordering Briyani")
            case _:
                print("Invalid input")
    case 3:
        display=int(input('''1 → Ice Cream
2 → Cake
3 → Gulab Jamun'''))
        match display:
            case 1:
                print("Ordering Ice Cream")
            case 2:
                print("Ordering Cake")
            case 3:
                print("Ordering Gulab Jamun")
            case _:
                print("Invalid input")
    case 4:
        display= int(input('''1 → Coffee
2 → Tea
3 → Juice'''))
        match display:
            case 1:
                print("Ordering Coffee")
            case 2:
                print("Ordering Tea")
            case 3:
                print("Ordering Juice")
            case _:
                print("Invalid input")
    case _:
        print("Invalid input")


#Q36
payment = int(input('''Enter input type \n
1 → UPI
2 → Card
3 → Wallet'''))

match payment:
    case 1:
        upi = int(input('''1 → Scan QR
2 → Enter UPI ID'''))
        match upi :
            case 1:
                print("QR Scanned")
            case 2:
                print("UPI ID Enterd")
            case _:
                print("Invalid input")
    case 2:
        card = int (input('''1 → Credit Card
2 → Debit Card'''))
        match card:
            case 1:
                print("Credit Card Selected")
            case 2:
                print("Debit Card Selected")
            case _:
                print("Invalid input")
    case 3:
        wallet = int(input('''1 → Add Money
2 → Pay Using Wallet'''))
        match wallet:
            case 1:
                print("Money Added")
            case 2:
                print("Payed using wallet")
            case _:
                print("Invalid input")
    case _:
        print("Invalid input")



#Q37
subject = int(input('''1 → Programming
2 → Mathematics
3 → Communication : '''))

match subject :
    case 1:
        sub = int(input('''1 → Python
2 → Java
3 → C++ : '''))
        match sub :
            case 1:
                print("Python Selected")
            case 2:
                print("Java Selected")
            case 3:
                print("C++ Selected")
            case _:
                print("Invalid input")
    case 2:
        sub = int(input('''1 → Algebra
2 → Calculus
3 → Statistics : '''))
        match sub:
            case 1:
                print("Algebra Selected")
            case 2:
                print("Calculus Selected")
            case 3:
                print("Statistics Selected")
            case _:
                print("Invalid Input")
    case 3:
        sub = int(input('''1 → English
2 → Presentation
3 → Interview Skills : '''))
        match sub:
            case 1:
                print("English SElected")
            case 2:
                print("Presentation Selected")
            case 3:
                print("Skills Selected")
            case _:
                print("Invalid input")
    case _:
        print("Invalid input")


#Q38
dashboard = int(input('''Enter a number for \n 
1 → Engine
2 → Lights
3 → Music
4 → Navigation'''))

match dashboard:
    case 1:
        option=int(input('''1 → Start
2 → Stop : '''))
        match option:
            case 1:
                print("Starting Engine")
            case 2:
                print("Engine Stopped")
            case _:
                print("Invalid input")
    case 2:
        option=int(input('''1 → Headlights
2 → Indicators
3 → Hazard Lights : '''))
        match option:
            case 1:
                print("Headlights On")
            case 2:
                print("Indicators Enabled")
            case 3:
                print("Hazard Lights Turned On")
            case _:
                print("Invalid Input")

    case 3:
        option=int(input('''1 → Play
2 → Pause
3 → Next
4 → Previous :'''))
        match option:
            case 1:
                print("Music Played")
            case 2:
                print("Music Paused")
            case 3:
                print("Next Track Started")
            case 4:
                print("Previous Track Switched")
            case _:
                print("Invalid input")
    case 4:
        option = int(input('''1 → Start Navigation
2 → Stop Navigation : '''))
        match option:
            case 1:
                print("Entering Navigation")
            case 2:
                print("Exiting Navigation")
            case _:
                print("Invalid input")
    case _:
        print("Invalid input")


#Q39
main_menu=int(input('''Select your designation \n
1 → Employee
2 → Manager :'''))

match main_menu:
    case 1:
        select=int(input('''Select an option \n
        1 → View Profile
2 → Apply Leave
3 → View Salary'''))
        match select:
            case 1:
                print("Profile Loading")
            case 2:
                days=int(input("Enter number of days :"))                
                if days >0:
                    print("Leave Granted")
                else:
                    print("Invalid Leave Days")    

            case 3:
                print("Salary loading")
            case _:
                print("Invalid input")

    case 2:
        select=int(input('''1 → View Team
2 → Approve Leave
3 → View Reports :'''))
        match select:
            case 1:
                print("Loading Team")
            case 2:
                print("Approving Leave")
            case 3:
                print("Reports Loading")
            case _:
                print("Invalid Input")
    case _:
        print("Invalid Input")



#Q40

# # exe_1
# age = int(input("enter your age: "))
# if age >=18:
#     print("Adult")
# else:
#     print("Minor")    

# # exe_2
# num = int(input("enter num:" ))
# if num >0:
#     print("Positive ")
# elif num <0:
#     print("Negative ")    
# else:
#     print("Zero ")

# # exe_3
# num = int(input("enter num:" ))
# if num %2==0:
#     print("even")
# else:
#     print("odd")    

# # exe_4
# nums = input("enter two nums: ")
# num1,num2 = nums.split(" ")
# if num1 > num2:
#     print(num1)
# elif num1<num2:
#     print(num2)
# else:
#     print("draw")        

# # exe_5
# password = "Python123"
# new_password = input("enter password: ")
# if new_password.strip().lower() == password.lower():
#     print("Access Granted")
# else:
#     print("Access Denied")    

# # exe_6
# num = int(input("enter num:" ))
# if num in range(1,11):
#     print("between 1-10")
# elif num in range(11,51):
#     print("between 11-50")
# elif num in range(51,100):
#     print("between 51-100")
# else:
#     print("out of range!!")       

# # exe_7
# grade = int(input("enter grade [0-100]: "))
# if grade in range(90,101):
#     print("Excellent")
# elif grade in range(80,90):
#     print("Very Good")    
# elif grade in range(70,80):
#     print("Good")
# elif grade in range(60,70):
#     print("Passed")
# elif grade in range(0,60):
#     print("Failed")            
# else:
#     print("Invalid Grade")    

# # exe_8
# correct_username = "admin"
# correct_password = "123456"
# info = input("enter username and password: ")
# username,password = info.strip(" ")
# if username == correct_username and password == correct_password:
#     print("Login Successful")
# elif username == correct_username and password != correct_password:
#     print("Wrong Password") 
# elif username != correct_username:
#     print("Unknown User")   

# # exe_9
# price = int(input("enter price: "))
# age = int(input("enter age: "))
# if age >60:
#     price = price - (price*0.2)
#     print(price)
# elif age <18:
#     price = price - (price*0.1)
#     print(price)
# else:
#     print(price)

# # exe_10
# num = int(input("enter num:" ))
# if num % 3 == 0 and num %5 !=0:
#     print(num)
# elif num % 5 == 0 and num %3!=0:
#     print(num)
# elif num % 5 == 0 and num % 3 ==0:
#     print(num)
# else:
#     print(num)

# # exe_11
# age = int(input("enter your age: "))
# with_old = bool(input("enter [true or false] you come with old man? "))
# if age >=18:
#     print("allowed")
# else:
#     if with_old == True:
#         print("allowed")
#     else:
#         print("not allowed!") 
 
# # exe_12
# avg_grades = float(input("enter avg grades: "))
# salary = float(input("enter salary: "))
# if avg_grades > 90:
#     print("entitled")
# elif avg_grades < 90 and salary <5000:
#     print("entitled")
# else:
#     print("not entitled")

# # exe_13
# correct_username = "admin"
# correct_password = "123456"
# info = input("enter username and password: ")
# username,password = info.strip(" ")
# is_active = bool(input("enter [true or false] is active? "))
# if username == correct_username and password == correct_password and is_active ==True:
#     print("allowed")
# else:
#     print("not allowed!") 

# # exe_14
# num = int(input("enter num:" ))
# if num in range(20,81):
#     print("in range")
# if not num > 80 and not num < 20:
#     print("in range")

# #  exe _15
# balance = 5000
# num = int(input("enter num to withdraw:" ))
# if num >0:
#     if not num > balance:
#         balance = balance-num
#         print(balance)
#     else:
#         print("you cant to withdraw!")
# else:
#     print("is not positive!!")

# # exe_16
# age = int(input("enter your age: "))
# club = bool(input("enter [true or false] you have club? "))
# if age <12:
#     if club == True:
#         price = 25 - (25*0.1)
#         print(price)
#     else:
#         print(25)
# elif age >=12 and age <18:
#     if club == True:
#         price = 35 - (35*0.1)
#         print(price)
#     else:
#         print(35)   
# else:
#     if club == True:
#         price = 50 - (50*0.1)
#         print(price)
#     else:
#         print(50)                

# # exe_17
# Seniority = int(input("enter your Seniority [month]: "))
# age = int(input("enter your age: "))
# salary = float(input("enter salary: "))
# if age >21:
#     if salary >=7000:
#         if Seniority >=12:
#             print("entitled")
#         else:
#             print("not enough Seniority")
#     else:
#         print("not enough salary")
# else:
#     print("not enough age")        

# # exe_18
# Vehicle_Type = input("enter Vehicle_Type[motorcycle,car,Commercial vehicle]: ")
# hours = int(input("enter hours to parking [minutes]: "))
# if Vehicle_Type.lower() == "motorcycle":
#     if hours <=60:
#         price = 10 - (10*0.1)
#         print(price*(hours/60))
#     elif hours > 300:
#         price = 10 - (10*0.15)
#         print(price*(hours/60))
#     else:
#         print(10*(hours/60))
# elif Vehicle_Type.lower() == "car":   
#     if hours <=60:
#         price = 20 - (20*0.1)
#         print(price*(hours/60))
#     elif hours > 300:
#         price = 20 - (20*0.15)
#         print(price*(hours/60))
#     else:
#         print(20*(hours/60))
# elif Vehicle_Type.lower() == "Commercial vehicle":   
#     if hours <=60:
#         price = 30 - (30*0.1)
#         print(price*(hours/60))
#     elif hours > 300:
#         price = 30 - (30*0.15)
#         print(price*(hours/60))
#     else:
#         print(30*(hours/60))        
# else:
#     print("not found!")

# # exe_19
# info = input("enter num1 num2 operator: ")
# num1,num2,operator = info.split(" ")
# match operator:
#     case "+":
#         add = int(num1) + int(num2)
#         print(add)
#     case "-":
#         sub =  int(num1) -int(num2)   
#         print(sub)
#     case "*":
#         multy = int(num1) * int(num2)  
#         print(multy)
#     case "/":
#         if num2 == 0:
#             print("not divide by zero!")
#         else:    
#             divide = int(num1) / int(num2)
#     case _:
#         print("not found!")   

# exe_20
year = int(input("enter year: "))
if year % 400==0:
    print("leap year")
elif year % 100 ==0 and year % 400 !=0:
    print("not leap year")
elif year % 4 ==0 and year % 100 !=0:
    print("leap year")
else:
    print("not leap year")

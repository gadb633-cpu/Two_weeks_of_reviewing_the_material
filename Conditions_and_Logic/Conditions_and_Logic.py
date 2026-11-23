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

# 
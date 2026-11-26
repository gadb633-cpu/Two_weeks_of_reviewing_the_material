# # exe 1
# def say_hello():
#     print("Hello world!")
# say_hello()
# say_hello()
# say_hello()

# # exe 2
# def show_welcome():
#     print("welcome!")
# show_welcome()     

# # exe 3
# def shaw_menu():
#     print('''
# ===== Main Menu =====
# 1. Start
# 2. Settings
# 3. Exit
# ''')

# # exe 4
# def show_numbers():
#     for i in range(11):
#         print(i) 

# # exe 5
# def show_even_numbers(): 
#     for num in range(101):
#         if num %2==0:
#             print(num)

# # exe 6
# def show_stars():
#     print("**********")
# for i in range(6):    
#     show_stars()    

# # exe 7
# def greet(name):
#     print("Hello", name)
# greet("David")
# greet("Moshe")

# # exe 8
# def show_age(age):
#     print(age)
# show_age(20)
# show_age(25)

# # exe 9
# def calculate_sum(num1,num2):
#     print(num1+num2)

# # exe 10
# def calculate_average(grade1,grade2,grade3):
#     print((grade1+grade2+grade3)/3)

# # exe 11
# def check_even(num):
#     if num%2==0:
#         print("even")
#     print("odd")    

# # exe 12
# def check_password(password):
#     if password == "123456":
#         print("Access Granted")
#     print("Access Denied")  

# # exe 13
# def calculate_discount(price,discount):
#     print(price-(price*discount))   

# # exe 14
# def show_range(num1,num2):
#     for num in range(num1,num2):
#         print(num)
# show_range(1,10)    

# # exe 15
# def print_rectangle(high,width):
#     for i in range(high):
#         print("*"*width,end="")
#         print()
# print_rectangle(3,5)

# # exe 16
# def multiply(num1,num2):
#     return num1*num2

# # exe 17
# def get_full_name(first_name,last_name):
#     return first_name+" "+last_name

# # exe 18
# def get_max(num1,num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2

# # exe 19
# def is_positive(num):
#     if num >0:
#         return True
#     return False

# # exe 20
# def calculate_tax(price,tax):
#     return price + (price * tax/100)

# # exe 21
# def get_grade_status(grade):
#     if grade >= 90:
#         return "Excellent "
#     elif grade >=75:
#         return "good"
#     elif grade >=60:
#         return "Average "
#     else:
#         return "Failed "

# # exe 22
# def count_digits(num):
#     return len(str(num))
# print(count_digits(1458787555)) 

# # exe 23
# def calculate_power(num,power):
#     result = num
#     for i in range(power-1):
#         result *=num
#     return result
# print(calculate_power(4,4))

# # exe 24
# def print_list(list_items):
#     for i in list_items:
#         print(i)

# # exe 25
# def get_list_sum(nums):
#     s=0
#     for num in nums:
#         s+=num
#     return s   

# # exe 26
# def get_list_average(nums):
#     if len(nums) == 0:
#         raise ZeroDivisionError("you cant to divide by zero!")
#     return sum(nums)/len(nums)

# def fibonacci(num):
#     f = [0,1]
#     for i in range(num-2):
#         f.append(f[-2]+f[-1])
#     print(f)
# fibonacci(10)    
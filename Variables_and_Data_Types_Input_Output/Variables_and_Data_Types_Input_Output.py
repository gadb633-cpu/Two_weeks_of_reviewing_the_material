# exe_1

first_name = "gad"
last_name = "biton"
age =24
city = "bny brak"
email = "gadb633@gmail.com"
print(f'''
    ===== User Details =====
    First Name: {first_name}
    Last Name: {last_name}
    Age: {age}
    City: {city}
    Email: {email}
    =======================
    ''')

# exe_2
birth_year = 2003
current_year  = 2026

print(f"You are approximately {current_year-birth_year} years old.")

# exe_3
width = 20
height  = 40
surface = width * height
Scope = (width *2) + (height*2)
print(f"surface is : {surface} | scope is : {Scope}")

# exe_4
name = "David"
age = 25
height = 1.78
is_student = True
salary = 8500

print(f'''
        {name} , {type(name)}
        {age} , {type(age)}
        {height},{type(height)}
        {is_student} , {type(is_student)}
        {salary} , {type(salary)}
    ''')

# exe_5
first_name = input("enter your first_name: ")
last_name = input("enter your last_name: ")
age =input("enter your age: ")
city = input("enter your city: ")
print(f'''
=======welcome======
First Name: {first_name}
Last Name: {last_name}
Age: {age}
City: {city}
''')

# exe_6
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
add = num1 + num2
sub = num1 - num2
multy = num1 * num2
divide = num1 / num2
print(f"""
add: {add}
sub: {sub}
multy : {multy}
divide: {divide}
""")

# exe_7
name_product = input("enter name_product: ")
price_product = int(input("enter price_product: "))
Quantity = int(input("enter Quantity: "))
print(f'''
====== Purchase Receipt ======
Product: {name_product}
Price: {price_product}
Quantity: {Quantity}
Total: {Quantity * price_product}
==============================
''')

# exe_9
name = input("enter your name: ")
num_hours_per_month = int(input("enter num hours: "))
price_per_hour = int(input("enter price_per_hour: "))
print(f'''
=======result=======
hi {name}
num hours is: {num_hours_per_month}
price_per_hour is: {price_per_hour}
total_price: {num_hours_per_month * price_per_hour}
''')

# exe_10
total_price = int(input("enter total price: "))
percent_tip = int(input("enter percent_tip: "))
num_of_clients = int(input("enter num_of_clients: "))
price_tip = (total_price * percent_tip)/100
print(f"tip: {price_tip}")
print(f"total price is : {total_price+price_tip}")
print(f"total price for each: {(total_price+price_tip)/num_of_clients}")

# exe_12
a= 10
b=20
c = a
a=b
b=c
print(a,b)

# exe_13
first_name = input("enter first name: ")
last_name = input("enter last name: ")
age = int(input("enter age: "))
name_university = input("enter name university: ")
course_name = input("enter course name: ")
num_month = int(input("enter num month: "))
price_month = int(input("enter price month: "))
print(f'''
    ================================
        STUDENT REGISTRATION
    ================================

    Student: {first_name} {last_name}
    Age: {age}
    Institution: {name_university}
    Course: {course_name}
    Duration: {num_month}
    Monthly Price: {price_month}

    Total Course Price: {num_month * price_month}

    ================================
    Registration completed!
    ================================
''')
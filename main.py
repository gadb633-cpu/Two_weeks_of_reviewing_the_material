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
operator = input("enter operator: ")
print(num1 , operator , num2)
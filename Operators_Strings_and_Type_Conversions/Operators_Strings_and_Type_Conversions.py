# # exe_1
# num1 = 25
# num2 = 7
# print(f'''
# add: {num1 + num2}
# sub: {num1 -  num2}
# multiplication: { num1 * num2}
# divide: {num1/num2}
# Integer division: {num1 // num2}
# Remainder of division: {num1 % num2}
# holding: {num1 ** num2}
# ''')

# # exe_2
# balance = 1000
# balance +=250
# print(balance)
# balance -=100
# print(balance)
# balance *=2
# print(balance)
# balance/=4
# print(balance)

# # exe_3
# price_product = int(input("enter price product: "))
# percent = int(input("enter percent: "))
# print(f'''
# price percent: {(price_product * percent)/100}
# finally price: {price_product - ((price_product * percent)/100)}
# ''')

# # exe_4
# price = int(input("enter price: "))
# Interest = int(input("enter Interest: "))
# print(f'''
# price Interest: {(price * Interest)/100}
# finally price: {price + ((price * Interest)/100)}
#  ''')

# # exe_5
# grades1 = float(input("enter grades1: "))
# grades2 = float(input("enter grades2: "))
# grades3 = float(input("enter grades3: "))
# print(f"avg: {(grades1 + grades2 +grades3) /3:.2f}")

# # exe_6
# first_name = "David"
# last_name = "Cohen"
# city = "Tel Aviv"
# print(f"Hello, my name is {first_name} {last_name} and I live in {city}.")
# print("Hello, my name is" + first_name +" "+ last_name + "and I live in" + city)

# # exe_7
# name = input("enter your name: ")
# print(name)
# print(len(name))
# print(name.lower())
# print(name.upper())

# # exe_8
# sentence = input("enter sentence: ")
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.capitalize())
# print(sentence.title())

# # exe_9
# name = input("enter name: ")
# print(name)
# print(len(name))
# print(name.strip())
# print(len(name.strip()))

# # exe_10
# sentence = "I love Java programming"
# new_sentence = sentence.replace("Java","python")
# print(new_sentence)
# print(new_sentence.count("love"))
# print(new_sentence.startswith("I"))
# print(new_sentence.endswith("programming"))

# # exe_11
# word = "Programming"
# print(word[0])
# print(word[-1])
# print(word[2:3])
# print(word[:3])
# print(word[-4:])
# print(word[::-1])

# # exe_12
# a = "100"
# b = "25"
# c = 10
# d = 5.5
# a = int(a)
# b = float(b)
# c = str(c)
# d = int(d)
# print(f"""
# {type(a)}
# {type(b)}
# {type(c)}
# {type(d)}
# """)

# # exe_13
# age = input("Enter your age: ")
# # לא תקין להוסיף int ל str 
# age = int(age)
# print(age +10)

# # exe_14
# Price_excluding_VAT = float(input("enter Price_excluding_VAT: "))
# total_price = Price_excluding_VAT + (Price_excluding_VAT*0.18)
# print(total_price)

# exe_15
first_name = input("enter first name: ")
last_name = input("enter last name: ")
age = int(input("enter your age: "))
salary = float(input("enter your salary: "))
num_of_years = int(input("enter num_of_years: "))
print(f"""
    =======result=======
    name: {first_name} {last_name}
    age: {age}
    salary: {salary}
    num of years: {num_of_years}
    """)
years_salary = salary *12
salary_with_bonus = salary + (salary *0.5)
len_full_name = len(first_name + last_name)
print(f'''
    years_salary: {years_salary}
    salary_with_bonus: {salary_with_bonus}
    len_full_name: {len_full_name}
''')
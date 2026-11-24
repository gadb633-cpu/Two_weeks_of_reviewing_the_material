# # exe 1
# numbers = (10, 20, 30, 40, 50)
# print(numbers)
# print(numbers[0])
# print(numbers[-1])
# print(len(numbers))
# print(numbers[2])

# # exe 2
# students = ("yossi", "gad", "chaim", "David", "moishi")
# for s in students:
#     print(s)
#     if s == "gad":
#         print("exists")    
# print(len(students))    

# # exe 3
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(numbers[:3])
# print(numbers[-3:])
# print(numbers[::-1])

# # exe 4-5
# car = ("tesla",200000,5,"private cars")
# print(car[0],car[1],car[2],car[3])

# # exe 6
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# sum_num = 0
# highest = numbers[0]
# count = 0
# for num in numbers:
#     sum_num +=num
#     if num > highest:
#         highest = num
#     if num %2==0:
#         count +=1
# print(f"sum: {sum_num} \nhighest: {highest} \neven: {count}")

# # exe 7
# products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")
# first_products = products[:3]
# last_products = products[-2:]
# new_products = first_products + last_products
# print(new_products)

# # exe 8
# student = {"name": "David","age": 22,"grade": 95,"city":"TLV"}
# print(student["name"],student["age"],student["grade"],student["city"])

# # exe 9
# car = {"brand":"tesla","model":"electric","year":2026,"price":200000}
# car["price"] = 250000
# car["year"] = 2027
# car["color"] = "green"
# print(car)

# # exe 10
# salaries = {"David": 12000,"Moshe": 15000,"Dana": 13500}
# for salary in salaries:
#     print(salaries[salary])
# salaries["David"] = 17000
# salaries["gad"] = 40000
# print(salaries)    
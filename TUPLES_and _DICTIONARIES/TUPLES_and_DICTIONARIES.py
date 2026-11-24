# exe 1
numbers = (10, 20, 30, 40, 50)
print(numbers)
print(numbers[0])
print(numbers[-1])
print(len(numbers))
print(numbers[2])

# exe 2
students = ("yossi", "gad", "chaim", "David", "moishi")
for s in students:
    print(s)
    if s == "gad":
        print("exists")    
print(len(students))    

# exe 3
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers[:3])
print(numbers[-3:])
print(numbers[::-1])

# exe 4-5
car = ("tesla",200000,5,"private cars")
print(car[0],car[1],car[2],car[3])

# exe 6
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sum_num = 0
highest = numbers[0]
count = 0
for num in numbers:
    sum_num +=num
    if num > highest:
        highest = num
    if num %2==0:
        count +=1
print(f"sum: {sum_num} \nhighest: {highest} \neven: {count}")

# exe 7
products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")
first_products = products[:3]
last_products = products[-2:]
new_products = first_products + last_products
print(new_products)

# exe 8
student = {"name": "David","age": 22,"grade": 95,"city":"TLV"}
print(student["name"],student["age"],student["grade"],student["city"])

# exe 9
car = {"brand":"tesla","model":"electric","year":2026,"price":200000}
car["price"] = 250000
car["year"] = 2027
car["color"] = "green"
print(car)

# exe 10
salaries = {"David": 12000,"Moshe": 15000,"Dana": 13500}
for salary in salaries:
    print(salaries[salary])
salaries["David"] = 17000
salaries["gad"] = 40000
print(salaries)    

# exe 11
products = {"apple": 2.5, "banana": 1.2, "orange": 3.0, "grape": 4.5}
name = input("enter name product: ")
found = False
for p in products:
    if name == p:
        found = True
        print(products[p])
if not found:
    print("not found!!")

# exe 12
students = {"David": 80,"Moshe": 87,"Dana": 91,"gad":100,"chaim":95}
for s in students:
    print(f"Student: {s} | Grade: {students[s]}")\

# exe 13
grades = {"David": 90,"Moshe": 75,"Dana": 100,"Noa": 55,"Avi": 82}

sum_grades = 0
highest = "David"
count = 0
for g in grades:
    sum_grades += grades[g]
    if grades[g] >80:
        print(g)
    if grades[g] > grades[highest]:
        highest= g
    if grades[g] <60:
        count +=1
print(sum_grades/len(grades))
print(f"highest: {highest}")
print(f"failed: {count}")

# exe 14
products = {"apple": 2.5, "banana": 1.2, "orange": 3.0, "grape": 4.5}
name = input("enter name product: ")
found = False
for p in products:
    if name == p:
        found = True
        price = int(input("enter new price: "))
        products[p] = price
if not found:
    price = int(input("enter price: "))
    products[name] = price
print(products)    

# exe 15
students = [    {"name": "David", "age": 20, "grade": 90},    {"name": "Moshe", "age": 22, "grade": 75},    {"name": "Dana", "age": 21, "grade": 100},    {"name": "Noa", "age": 19, "grade": 55},    {"name": "Avi", "age": 23, "grade": 82}]
sum_grades = 0
highest = students[0]
for s in students:
    sum_grades += s["grade"]
    print(s["name"])
    print(s["grade"])
    if s["grade"] >80:
        print(f"Over 80: {s["name"]}")
    if s["grade"] >highest["grade"]:
        highest = s
avg = sum_grades / len(students)    
print(f"avg: {avg}")
print(f"highest: {highest["name"]}")

# exe 16
students = [{"name": "David", "age": 20, "grade": 90},{"name": "Moshe", "age": 22, "grade": 75},{"name": "Dana", "age": 21, "grade": 100},{"name": "Noa", "age": 19, "grade": 55},{"name": "Avi", "age": 23, "grade": 82}]
students.append({"name":"gad","age":24,"grade":99})
students[0]["grade"] = 92
for s in range(len(students)):
    if students[s]["name"] == "Moshe":
        students.pop(s)
        break
print(students)   
 
# exe 17
classroom = {"Class A": ["David", "Moshe", "Dana"],"Class B": ["Noa", "Avi", "Michael"],"Class C": ["Daniel", "Shir", "Yossi"]} 
classroom["Class B"].append("gad")
classroom["Class C"].pop(0)
for c in classroom:
    print(c)
    print(classroom[c])
    print(len(classroom[c]))

# exe 18
products = {"Laptop": {"price": 4500,"stock": 10},"Mouse": {"price": 80,"stock": 50},"Keyboard": {"price": 150,"stock": 20}}
products["Laptop"]["stock"] = 25
products["phone"] = {"price":6500,"stock":57}   
for p in products:
    print(products[p]["price"])
    print(products[p]["stock"])
    if products[p]["price"] > 100:
        print(f"over 100: {p}")

# exe 19
employees = [("David", "Development", 15000),("Moshe", "Marketing", 12000),("Dana", "Development", 18000),("Noa", "HR", 11000)]
highest = employees[0]
sum_salary = 0
for employ in employees:
    sum_salary += employ[2]
    print(employ[0])
    if employ[1]=="Development":
        print(employ)
    if employ[2] > highest[2]:
        highest = employ
print(f"highest:{highest[0]}")  
print(f"avg: {sum_salary/len(employees)}")      

# exe 20
inventory = {"Laptop": 10,"Mouse": 50,"Keyboard": 20}
name,amount = input("enter name and quantity: ").split(" ")
if name not in inventory:
    print("not found!")
elif inventory[name] < int(amount):
    print("not enough!")
else:
    inventory[name] -= int(amount)
    print(inventory)

# exe 21
votes = {"David": 0,"Moshe": 0,"Dana": 0}
while True:
    name = input("enter name to vote: ")
    if name.lower().strip() =="stop":
        winner = "David"
        print(votes)
        for vote in votes:
            if votes[vote] > votes[winner]:
                winner = vote
        print(f"winner: {winner}")        
        break
    if name not in votes:
        print("not exist")
        continue
    votes[name] +=1    

# exe 22
contact = {"gad":"0504114558","chaim":"0583454748","moshe":"054256987"}
while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Show all contacts")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contact[name] = phone
        print(f"Contact {name} added.")
        
    elif choice == "2":
        name = input("Enter name to search: ")
        if name in contact:
            print(f"{name}: {contact[name]}")
        else:
            print("not found")
            
    elif choice == "3":
        name = input("Enter name to update: ")
        if name in contact:
            phone = input("Enter new phone number: ")
            contact[name] = phone
            print(f"Contact {name} updated.")
        else:
            print("not found.")
            
    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contact:
            del contact[name]
            print(f"Contact {name} deleted.")
        else:
            print("not found.")
            
    elif choice == "5":
        for name, phone in contact.items():
            print(f"{name}: {phone}")
            
    elif choice == "6":
        break
    else:
        print("only 1-6")

# exe last
products = [
    {"name": "Laptop", "price": 4500, "stock": 10},
    {"name": "Mouse", "price": 80, "stock": 50},    
    {"name": "Keyboard", "price": 150, "stock": 20},
    {"name": "Screen", "price": 900, "stock": 15}]
while True:
    print('''
    ===== Store Management =====

    1. Show all products
    2. Add product
    3. Search product
    4. Update product price
    5. Update product stock
    6. Sell product
    7. Show products by price
    8. Show products with low stock
    9. Show total inventory value
    0. Exit
    ''')
    choice = input("enter your choice: ")
    if choice == "1":
        for product in products:
            print(f"Name: {product["name"]}, Price: {product["price"]}, Stock: {product["stock"]}") 
    if choice == "2":
        name = input("enter product name: ")
        price = int(input("enter product price: "))
        stock = int(input("enter product stock: "))
        products.append({"name": name, "price": price, "stock": stock})
    if choice == "3":
        name = input("enter product name to search: ")
        found = False
        for product in products:
            if product["name"] == name:
                found = True
                print(f"Name: {product["name"]}, Price: {product["price"]}, Stock: {product["stock"]}")
        if not found:
            print("not found.") 
    if choice == "4":
        name = input("enter product name: ")
        found = False
        for product in products:
            if product["name"] == name:
                found = True
                new_price = int(input("enter new price: "))
                product["price"] = new_price
                print(f"Price updated for {name}.")
        if not found:
            print("not found.")
    if choice == "5":
        name = input("enter product name: ")
        found = False
        for product in products:
            if product["name"] == name:
                found = True
                new_stock = int(input("enter new stock: "))
                product["stock"] = new_stock
                print(f"Stock updated for {name}.")
        if not found:
            print("not found.")
    if choice == "6":
        name = input("enter product name: ")
        found = False
        for product in products:
            if product["name"] == name:
                found = True
                quantity = int(input("enter quantity: "))
                if product["stock"] >= quantity:
                    product["stock"] -= quantity
                    print(f"Sold {quantity} of {name}.")
                else:
                    print("Not enough stock.")
        if not found:
            print("not found.")
    if choice == "7":
        price = int(input("enter price: "))
        expensive_products = [product for product in products if product["price"] > price]
        for product in expensive_products:
            print(f"Name: {product["name"]}, Price: {product["price"]}, Stock: {product["stock"]}") 
    if choice == "8":
        low_stock_products = [product for product in products if product["stock"] < 10]
        for product in low_stock_products:
            print(f"Name: {product["name"]}, Price: {product["price"]}, Stock: {product["stock"]}")
    if choice == "9":
        total_value = sum(product["price"] * product["stock"] for product in products)
        print(f"Total value: {total_value}")
    if choice == "0":
        break
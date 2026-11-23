# # exe_1
# numbers = [10,20,30,40,50]
# print(numbers)
# print(numbers[0])
# print(numbers[-1])
# print(numbers[2])

# # exe 2
# students = ["yossi", "gad", "chaim", "David", "moishi"]
# print(len(students))
# print(students[0])
# print(students[-1])
# students[1] = "biton"
# print(students)

# # exe 3
# grades = [85, 90, 78, 92, 88]
# grades.append(95)
# grades.insert(0, 80)
# grades[2] = 82
# print(grades)

# # exe 4
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers)
# del numbers[0]
# print(numbers)
# del numbers[-1]
# print(numbers)
# del numbers[3]
# print(numbers)

# # exe 5
# products = ["apple", "banana", "orange", "computer", "phone"]
# if "apple" in products:
#     print("Apple exists in the list")
# if "milk" not in products:
#     print("Milk not exist in the list")

# # exe 6
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     print(num)

# # exe 7
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)

# # exe 8
# grades = [85, 90, 78, 92, 88]
# total = 0
# for grade in grades:
#     total += grade
# print(total)

# # exe 9
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# max_number = numbers[0]
# for num in numbers:
#     if num > max_number:
#         max_number = num
# print(max_number)

# # exe 10
# students = ["yossi", "gad", "chaim", "David", "moishi"]
# name = input("Enter name: ")
# found = False
# for student in students:
#     if student == name:
#         print("Found")
#         found = True
#         break
# if not found:
#     print("Not Found")

# # exe 11
# numbers = [10, 20, 30, 40, 20]
# num = int(input("Enter a number: "))
# indexes = []
# for i in range(len(numbers)):
#     if numbers[i] == num:
#         indexes.append(i)
# if indexes:
#     print(indexes)
# else:
#     print("Number not found")

# # exe 12
# numbers = [15, 20, 32, 40, 20, 62, 70, 85, 90, 98]
# count = 0
# for num in numbers:
#     if num > 50:
#         count += 1
# print(count)

# # exe 13
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
# print(even_numbers)

# # exe 14
# students = ["yossi", "gad", "chaim", "David", "moishi"]
# i = 0
# while i < len(students):
#     print(f"Index: {i}, Name: {students[i]}")
#     i += 1

# # exe 15
# numbers = [5, 10, 18, 20, 26, 32, 35, 43, 47, 50]
# print(numbers[:3])
# print(numbers[-3:])
# print(numbers[2:7])
# print(numbers[::-1])

# # exe 16
# students = ["yossi", "gad", "chaim", "David", "moishi", "shlomo", "rivka", "avraham", "Sarah", "Moshe"]
# print("even")
# for i in range(0, len(students), 2):
#     print(students[i])
# print("odd")
# for i in range(1, len(students), 2):
#     print(students[i])
# print(students[::-2])

# # exe 17
# numbers = [1, 22, 83, 4, 5, 65, 7, 48, 9, 41, 11, 17, 13, 34, 15, 16, 17, 18, 54, 56]
# first_10 = numbers[:10]
# last_10 = numbers[-10:]
# list_5_14 = numbers[5:15]

# # exe 18
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num_list = len(numbers) // 2
# first = numbers[:num_list]
# last = numbers[num_list:]

# # exe 19
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# doubled = [num * 2 for num in numbers]
# squared = [num ** 2 for num in numbers]
# even_numbers = [num for num in numbers if num % 2 == 0]
# large_numbers = [num for num in numbers if num > 5]

# # exe 20
# grades = [55, 90, 67, 100, 45, 82, 73, 30]
# passed = [grade for grade in grades if grade > 60]
# failed = [grade for grade in grades if grade < 60]
# grades_add_5 = [grade + 5 for grade in grades]

# # exe 21
# names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]
# long_names = [name for name in names if len(name) > 4]
# uppercase_names = [name.upper() for name in names]
# d_names = [name for name in names if name.startswith("D")]

# # exe 22
# numbers = [12, 7, 25, 30, 9, 44, 18, 3]
# new_list = [num for num in numbers if num % 3 == 0 and num > 10]
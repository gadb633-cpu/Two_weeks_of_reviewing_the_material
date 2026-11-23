# # exe_1
# count = 1
# while count <=10:
#     print(count)
#     count +=1

# # exe_2
# count = 10
# while count <=10 and count >0:
#     print(count)
#     count -=1
# print("START!")  

# # exe_3
# count = 1
# while count in range(1,51):
#     if count %2==0:
#         print(count)
#     count +=1

# # exe_4
# num = int(input("enter num: "))
# count = 1
# while count !=5:
#     print(num * count)
#     count +=1

# # exe_5
# sum_nums = 0
# count = 1
# while count !=101:
#     sum_nums +=count
#     count +=1
# print(sum_nums)    

# # exe_6
# correct_password = "Python123"
# while True:
#     password = input("enter password: ")
#     if password.lower() == correct_password.lower():
#         print("Welcome!")
#         break

# # exe_7
# secret_number = 27
# while True:
#     guess_num = int(input("enter guess_num: "))
#     if guess_num == secret_number:
#         print("success!")
#         break

# # exe_8
# sum_num = 0
# while True:
#     num = int(input("enter num: "))
#     if num <= 0:
#         print(sum_num)
#         break
#     sum_num +=num

# # exe_9
# count = 0
# sum_grades = 0
# while True:
#     grade = int(input("enter grade: "))
#     if grade == 999:
#         break
#     count +=1
#     sum_grades += grade
# print(f"count grades: {count} \nsum_grades: {sum_grades} \navg: {sum_grades/count}")    

# # exe_10
# sum_num = 0
# count = 0 
# while True:
#     num = int(input("enter num: "))
#     if num < 0:
#         print(sum_num)
#         print(count)
#         break
#     sum_num +=num
#     count +=1

# # exe_11 
# num = int(input("enter num: "))
# count = 1
# while True:
#     if count > 10:
#         break
#     print(num *count)
#     count +=1

# # exe_12
# num = int(input("enter num: "))
# count = 0
# while num > 0:
#     count +=1
#     num //= 10
# print(count)    

# # exe_13
# num1 = int(input("enter num: "))
# count = 0
# while num1 > 0:
#     num2 = num1 % 10
#     num1 //=10
#     count *=10
#     count +=num2
# print(count)  

# # exe_14
# num1 = int(input("enter num: "))
# status = True
# count =2
# while count !=10:
#     if count == num1 !=2:
#         count+=1
#         continue
#     if num1 %1==0  and num1 %num1 ==0 and num1%count!=0:
#         count+=1 
#         continue   
#     else:
#         status = False
#         break
# print(status)     

# exe_15
balance = 5000
while True:
    print("""
    1. check balance
    2. deposit
    3. attract
    4. exit
    """)
    num = input("enter choice: ")
    match num:
        case "1":
            print(balance)
        case "2":
            amount = int(input("enter amount: "))
            if amount <=0:
                print("only positive")
                continue
            balance +=amount
        case "3":
            amount = int(input("enter amount: "))
            if amount <=0:
                print("only positive")
                continue
            if amount > balance:
                print("its bigger")  
                continue
            balance -= amount
        case "4":
            break      

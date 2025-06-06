#syntax
# for variable in sequence:
#     # code to be executed

# employee_data = ["harika",'kala',"karthik","koushik"]
# for i in employee_data:
#     print(f"{i} you are invited to the company anniversary")


# employee_id = (12,23,34,45,56,78)
# for i in employee_id:
#     print(f"employe id {i} you are invited to the party..")



# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)



# sample = "pythonlife"
# for i in sample:
#     print(i)

#range function syntax -- to generate sequence of numbers
# Syntax:
# range(stop)
# range(start, stop)
# range(start, stop, step)

# for i in range(11):
#     print(i)

# for i in range(10,100):
#     print(i)


# for i in range(99,1000):
#     print(i)


# for i in range(0,11,5):
#     print(i)



# for i in range(100,1001,2):
#     print(i)


# for i in range(-10,1,2):
#     print(i)

#multiplication of tables
# num = int(input("enter the multiplication: "))
# for i in range(1,21):
#     print(f"{num} X {i} = {i*num}")




# # #for i in iterable:
# #     for j in iterable:



# for i in range(4):#outer for loop
#     for j in range(4):#inner for loop





# for i in range(1,11): #outer for loop
#     for j in range(1,21):
#         print(f"{i} X {j} = {i*j}")
#     print("-"*15)




#syntax
# while condition:
#     # code to be executed

# age = 25
# while age>=18:
#     print("hello everyone")


# count = 0
# while count<3:
#     print(count)
#     count +=1 


# while True:
#     user_name = input("enter the username: ")
#     password = input("enter the password: ")
#     if user_name == "akhil" and password == "akhil@123":
#         print("login success")
#         break
#     else:
#         print("invalid login credentials...")


# product_list = [99,105,499,999,1999]
# for i in product_list:
#     print(i+1)



# Syntax:
# while outer_condition:
#     # outer loop code
#     while inner_condition:
#         # inner loop code


# while True:
#     print("hello everyone")
#     while True:
#         print("welcome to pythonlife ")
#         break
#     break


# outer = 0
# while outer < 3:
#     inner = 0
#     while inner < 2:
#         print(outer, inner)
#         inner += 1
#     outer += 1

# sum = 0
# for i in range(1,6):
#     result = i**2
#     sum += result
# print(f"sum of numbers 1 to 5 is {sum}")


# count = 5
# while count>0:
#     print(count)
#     count -=1

# for i in range(1,6):
#     print("*"*i)

# rows = 4
# for i in range(1,rows+1):
#     print(" "*(rows - i) + "*" * (2*i-1) )

# print(" "*5)
# print(" "*(4)+"*"*(2*i-1))
# Syntax:
# if condition:
#      statement 1
#      statement 2
#      statement n

# age = 25
# if age>=18:#True  #false
#     print(f"you are eligible to vote your age is {age}")
#     print("you are adult")
#     num_1 = 10
#     num_2 = 10
#     result = num_1 + num_2
#     print(result)

# print(80+80)
# print("hello")


# age = 25
# if age>=18:#True  #false
#     print(f"you are eligible to vote your age is {age}")


# Syntax:
# if condition:
#     # code block to execute if condition is true
# else:
#     # code block to execute if condition is false

# age = 11
# if age>=18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")



# Syntax:
# if condition-1:  
#     statement 1 
# elif condition-2:
#     stetement 2 
# elif condition-3:
#     stetement 3 
#     ...         
# else:            
#     statement




#grading system
# marks = int(input("enter the marks 0-100: "))
# if marks>=90 and marks<=100:
#     print(f"you got A grade obtained marks {marks}")
# elif marks>=80 and marks>=89:
#     print(f"you got B grade obtained marks {marks}")
# elif marks>=70 and marks>=79:
#     print(f"you got C grade obtained marks {marks}")
# elif marks>=60 and marks>=59:
#     print(f"you got D grade obtained marks {marks}")
# elif marks>=35:
#     print(f"you got P grade obtained marks {marks}")
# elif marks<=34 and marks>=0:
#     print(f"you got F grade obtained marks {marks}")
# else:
#     print("invalid inputs")



user_name = input("enter the username: ")
password = input("enter the password: ")
if user_name == "phani" and password == "phani@123":
    print("login success")
else:
    print("invalid login credentials...")


# Syntax:
# if condition1:
#     # code block for condition1
#     if condition2:
#         # code block for condition2
#     else:
#         # code block for condition2 being false
# else:
#     # code block for condition1 being false

# if False:
#     print("this is if block: ")
#     if False:
#         print("this is nested if block")
#     else:
#         print("this is else block")
# else:
#     print("if block false statement")


# user_name = input("enter the username: ")
# password = input("enter the password: ")
# if user_name == "ramya":
#     if password == "ramya@1234":
#         print(f"login successful logged as {user_name}")
#     else:
#         print("invalid password......")
# else:
#     print("invalid username.......")




# age = 25
# if age>=18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")
# Syntax:
# result = value_if_true if condition else value_if_false

# result = "you are eligible to vote" if age>=18 else "you are not eliglbe to vote"
# print(result)
# print("you are eligible to vote") if age>=18 else print("you are not eligible to vote")

# num = int(input("enter the number: "))
# if num%2==0:
#     print("even number")
# else:
#     print("not even")

# print("even") if num%2==0 else print(" not even")







# Write a Python program that takes a character as input and checks whether it is a vowel or not. Use the if-else statement.
# char = input("enter the character: ")
# vowels = "aeiouAEIOU"
# if char in vowels:
#     print("vowel")
# else:
#     print("not vowel")


# char = input("enter the character: ")
# if char in "AEIOUaeiou":
#     print("vowel")
# else:
#     print("not vowel")

# char = input("enter the character: ")
# if char in ["a","e","i","o","u"]:
#     print("vowel")
# else:
#     print("not vowel")
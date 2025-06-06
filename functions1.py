#Syntax
# def funcname():
#     #block of code
#     #block of code


    # print("welcome to pythonlife")

# def sample(): #function definition
#     print("welcome to pythonlife.....")#block of code or function body
# sample() #function calling (  calling by the function name with pair of parenthesis)
# sample()
# sample()
# sample()
# sample()

# def add():
#     num_1 = 10
#     num_2 = 10
#     result = num_1 + num_2
#     print(result)
# add()

# def details():
#     user_name = input("enter the name")
#     id = int(input("enter id"))
#     print(user_name)
#     print(id)
# details()


# def mul(num1,num2):#function definition (parameters given within in the parenthesis)
#     result = num1 * num2
#     print(result)
# mul(10,20) #arguments passed to the paremeters during function call
# mul(50,20) #arguments passed to the paremeters during function call
# mul(10,5) #arguments passed to the paremeters during function call
# mul(2,2) #arguments passed to the paremeters during function call
# mul(12,2) #arguments passed to the paremeters during function call



#arbitary arguments--> function can accept a variable number of arguments by using *args(syntax)

# def sample(*a):
#     print(a)
# sample("vasu","venkatesh","amruth","kalyan",5.7,25)

# a = 1,2,3,4,5
# print(a)


#keyword arguments :-->keyword arguments are passed to a function with a keyword and a value, allowing for more explicit parameter passing
#**
# def greet(**a):
#     print(a)
# greet(a=10,b=20,c=30)

#* --> tuple
#** --> dictionary

def add(a,b):
    return a+b
obj = add(10,20)
# print(obj*30)


# def add(a,b,c):
#     return a+b+c
# obj = add(5,5,5)
# print(obj)

# def greet(user_name=None, id=None,dept=None,mail= "vasu@gmail.com"):
#     print(user_name,id,dept,mail)
# greet("harika",1234,"python","abc@gmail")
# greet("vasu",234,)
# greet("raju",)
# greet()


# def expo(a,b=5):
#     return a**b
# print(expo(5,))
# print(expo(10,))
# print(expo(50,))
# print(expo(25,6))

#variables  --> two types ---> local variables ---> global variable
#1. local variable ---> function ( inside the function)


# def details():
#     user_name = "amruth" #local variables
#     id = 534 #local variables
#     print(user_name,id)
#     num_1 = 50
#     print(num_1)
#     result = num_1+100
#     print(result)
# details()





# Global Variable:
# A variable declared outside of all functions and accessible throughout the program, including inside functions, is called a global variable.

# balance = 1000
# def credit(amount):
#     id = 1234
#     print(id)
#     print(amount)
#     print(balance)
# credit(500)

# print(balance*20)



# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def expo(a,b):
#     return a**b






# def credit():
# def withdraw():
# def bal():
# def mini():


# balance = 1000
# def credit(amount):
#     global balance
#     balance+=amount
#     print(balance)
# credit(500)
# def withdraw():
#     if balance>0:


# def square(a):
#     return a*a
# num_1 = int(input("enter the number:"))
# obj = square(num_1)
# print(f" {obj}")


# words = ["sports", "car", "break", "python", "skip", "code"]
# for i in words:
#     if i == "break":
#         break
#     elif i == "skip":
#         continue
# print(i)


# for i in range(2):
#     print(i)
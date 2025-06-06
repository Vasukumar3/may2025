#syntax:
# lambda arguments: expression
# def add(a,b): #function definition
#     return a+b
# obj = add(10,10)
# print(obj)

# lambda arguments: expression
# result = lambda a,b,c:a+b+c
# print(result(10,10,10))

# result = lambda x,y:x*y
# print(result(5,10))


# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24]
# empty_list = []
# for i in list_1:
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)

# Syntax:
# filter(function, iterable)
# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24]
# def even(a):
#     return a%2==0
# obj = filter(even,list_1)
# print(list(obj))

# lambda arg:exp
# filter(function, iterable)
# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24]
# result = filter(lambda a:a%2==0,list_1)
# print(list(result))



# Syntax:
# map(function, iterable, ...)

# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24,24]
# empty_list = []
# for i in list_1:
#     result = i*i
#     empty_list.append(result)
# print(empty_list)



# map(function, iterable, ...)
# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24,24]
# def square(a):
#     return a*a
# obj = map(square,list_1)
# print(list(obj))


# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24,24]
# list_2 = [25,45,22,58,96,10,58,1,2,36,79,24,24]
# map(func,iterable,) #task ----> two iterables



# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24,24]
# obj = map(lambda a:a*a,list_1)
# print(list(obj))

# from functools import reduce
# reduce(function, iterable[, initializer])#initializer--optional

# def add(a,b,c,d,e):
#     return a+b+c+d+e
# obj = add(10,10,5,2,5)
# print(obj)

from functools import reduce
# reduce(function, iterable[, initializer])#initializer--optional
# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24,24]
# def add(a,b):
#     return a+b
# result = reduce(add,list_1)
# print(result)


# from functools import reduce
# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24,24]
# obj = reduce(lambda a,b:a+b,list_1)
# print(obj)



"""
generator function --  a genetor -function is defined like a normal function
but whenever its need to generate a value
it does so with the yeild keyword rather than return
if body contain yield , the function  automatically
becomes a generator function.
"""

# def sample():
#     yield 1 #hold or pause
#     yield 2 #hold or pause
#     yield 3 #hold or pause
#     yield 4 #hold or pause
# obj = sample()
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())



# def factorial(n):
#     fact = 1
#     while n>1:
#         fact*=n
#         n -=1
#     return fact
# num = int(input("enter the number: "))
# if num>1:
#     print(f"fact of {num}, is {factorial(num)}")
# else:
#     print("enter positive integer")


# lambda arg:exp
# from functools import reduce
# # reduce(func,iter)
# def calculate_factorial(n):
#     return reduce(lambda x,y:x*y, range(1,n+1))
# num = int(input("enter the number: "))
# if num>0:
#     print(f"fact of {num}, is {calculate_factorial(num)}")
# else:
#     print("enter positive integer")
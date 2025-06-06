#3 types of errors
#1. syntax errors
#2. runtime errors
#3. logical errors --> user need to be identified (very difficult to find these errors)


#add of two numbers
# num_1 = 10
# num_2 = 20
# result = num_1 + num_2
# print(result)


#syntax errors
# for i in range(10):
#     print(i)


#2. runtime errors which disturbs the flow of execution ( during the execution ) also called exceptions\


# num_1 = int(input("enter the number 1: "))
# num_2 = int(input("enter the number 2: "))
# print(num_1+num_2)
# try:
#     print(num_1/num_2) 
# except:
#     print("error occured")
# print(num_1-num_2) 
# print(num_1*num_2) 



# list_1 = [1,2,3,4,5]
# print(list_1[4]) #5
# try:
#     print(list_1[6]) #5
#     print(list_1[8]) #5
# except:
#     print("list error occured")
# print(list_1[2]) #3


# list_1 = [1,2,3,4,5]
# try:
#     print(list_1[8])
# except Exception as e:
#     print(e)
# print(list_1[2])
# print(list_1[1])



# num_1 = int(input("enter the number 1: "))
# num_2 = int(input("enter the number 2: "))
# print(num_1+num_2)
# try:
#     print(num_1/num_2) 
# except Exception as e:
#     print(e)




# my_list = [10, 20, 30, 40]
# print(my_list[3])
# try:
#     print(my_list[10])
# except Exception as e:
#     print(e)
# else:
#     print(my_list[1])
# finally:
#     print("this is finally block")


# try:
#     a = int(input("enter the number:"))
#     print(a)

# except ValueError as e:
#     print(e)




try:
    pass# code that might raise a FileNotFoundError
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
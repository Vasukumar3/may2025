# list_1 = [1,2,3,"python",5.7,True,]
# # print(type(list_1))
# print(list_1[3])
# print(list_1[5])


# list_2 = []
# print(type(list_2))

# list_3 = list()
# print(type(list_3))

# my_list = [10, 20, 30, 40, 50]
# #syntax
# # var[index]
# print(my_list[1]) #20
# print(my_list[4]) #50
# print(my_list[3]) #40


# my_list = [10, 20, 30, 40, 50]
# print(my_list[-5])#10
# print(my_list[0])#10
# print(my_list[-1])#50
# print(my_list[4])#50
# print(my_list[-2])#40
# print(my_list[3])#40


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[1:7])
# print(my_list[2:5])
# print(my_list[0:7])
# print(my_list[0:8])



# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[:3])
# print(my_list[2:])
# print(my_list[0:8])
# print(my_list[::])




# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[2:5])
# print(my_list[-6:-3])
# print(my_list[4:7])
# print(my_list[-4:-1])



# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[-3:])
# print(my_list[::1])
# print(my_list[::-1])
# print(my_list[5:2:-1])
# print(my_list[-3:-6:-1])
# print(my_list[3:0:-1])
# print(my_list[-5:-8:-1])



# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[::3])
# print(my_list[::-3])


#.methodname(args)
# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# my_list.append([1,2,3,5.7,22,"vasu","python",])
# print(my_list)



# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# my_list.extend([1,2,3,5.7,22,"vasu","python",])
# print(my_list)

# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# sample = my_list.copy()
# sample.append("raja")
# print(sample)
# print(my_list)


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# my_list.clear()
# print(my_list)

# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list.count(20))

# voter_list = ["srinu","srinu","srinu","vasu","raja",'raja',"kiran","kumar"]
# print(voter_list.count("srinu"))

# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,1,1]
# print(numbers.index(1))


# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,1,1]
# numbers.remove(1)
# print(numbers)


# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,1,1]
# obj = numbers.pop(5)
# numbers.insert(5,"kalyan")
# print(numbers)
# print(obj*50)


# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,1,1]
# numbers.insert(5,"pythonlife")
# print(numbers)

# numbers = [1,3, 4, 1, 5, 9, 2, 6, 5,1,1,1]
# print(len(numbers))
# numbers.reverse()
# print(numbers)


# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,1,1]
# numbers.sort(reverse=True)
# print(numbers)


# list_1 = [1,2,3,4]

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[0][1])
# print(matrix[2][2])
# print(matrix[1][0])

# Syntax
# [expression for item in iterable]

# empty_list = []
# for i in range(11):
#     result = i*i
#     empty_list.append(result)
# print(empty_list)   
# 

# [exp for item in iterable]
# result = [i*i for i in range(11)]
# print(result)
# print([i*i for i in range(11)])

# empty_list = []
# for i in range(11):
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)

# [exp for item in iterable if condition]
# result = [i for i in range(11) if i%2==0]
# print(result)
# print([i for i in range(11) if i%2==0])



# my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(len(my_list))

# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,1,1]
# empty_list = []
# for i in numbers:
#     if i==1:
#         numbers.remove(i)
# print(numbers)


# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,1,1]
# numbers.remove(1)
# print(numbers)

# my_list = [3, 4, 1, 5, 9, 2, 6, 5,1,1,1,1]
# empty_list = []
# for i in my_list:
#     if i!=1:
#         empty_list.append(i)
# print(empty_list)

# result = [i for i in my_list if i!=1]
# print(result)

# print([i for i in my_list if i!=1])


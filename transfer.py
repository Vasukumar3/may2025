#break
# for tv in seq:
#     if condition:
#         break


# for i in range(11):
#     if i == 5:
#         break
#     # print(i)
# print(i)    


# for i in range(1,5):
#     if i%2==0:
#         break
# print(i)



# emp_id = [241,55,689,782,969,544,12,1,23,4,56]
# for i in emp_id:
#     if i == 55:
#         print(i)
#         break
# print(i)


# for item in iterable:
#     if condition:
#         continue

# for i in range(11):
#     if i == 7:
#         continue
#     print(i)
# print(i)


# product = ["ok","ok","ok","ok","ok","defect","ok","ok","defect","ok"]
# for i in product:
#     if i == "defect":
#         continue
#     print(i)
# print(i)

# for i in range(1,500):
#     if i%2==1:
#         continue
#     print(i)



# for i in range(0,500,2):
#     print(i)
    


# if condition:
#     pass


# for i in seq:
#     #block of code

# for i in range(10):
#     pass


# num = 25
# if num>=18:
#     pass
# else:
#     print("alternative block of code")
#     print(num*5)


numbers = [25, 30, 20, 40, 15, 25]
sum = 0
for i in numbers:
    sum+=i
    if sum >= 100:
        break
print(f"sum exceed 100, sum value {sum}")
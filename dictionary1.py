# dict_1 = {
#     1:"vasu",
#     2:"amruth",
#     3:"vali",
#     4:"subbu",
#     "id":123,
#     (1,2):"tuples",
#     5:[1,2,3],
#     "employee_id": 1234,
#     "EMPLOYEE_ID" : 4567,
# }
# print(dict_1)


# dict_2 = {
# }
# print(type(dict_2))

# dict_3 = dict()
# print(type(dict_3))


# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# dictionary_1.clear()
# print(dictionary_1)
# obj = dictionary_1.copy()
# print(obj)
# obj.clear()
# print(obj)
# print(dictionary_1)


# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# print(dictionary_1.items())
# print(dictionary_1.keys())
# print(dictionary_1.values())


# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# dictionary_1.pop("user3")
# print(dictionary_1)


# list_1 = [1,2,3,4]
# list_1.pop(2)
# print(list_1)



# list_1 = [1,2,3,4]
# print(list_1[3])



# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# print(dictionary_1["user3"])
# print(dictionary_1["user1"])
# print(dictionary_1.get("user3"))
# print(dictionary_1.get("user1"))




# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# print(dictionary_1["user5"])
# print(dictionary_1.get("user5"))


# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# sample = {
#     "user5":"user5@123",
#     "user6":"user6@123",
# }

# dictionary_1.update(sample)
# print(dictionary_1)
# print(sample)



# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# dictionary_1["user5"] = "user5@123"
# dictionary_1["user6"] = "user6@123"
# print(dictionary_1)
# dictionary_1.update({"user7":"user7@123"})
# print(dictionary_1)



# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# dictionary_1["user3"] = "vasu kumar"
# dictionary_1["user5"] = "user5@123"
# print(dictionary_1)

dict_1 = {

}
employee_id = int(input("enter the employe id: "))
user_name = input("enter the user name :")
dict_1[employee_id] = user_name
print(dict_1)
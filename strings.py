# Creating strings
# single_quoted_string = 'Hello, World! 8 Oclock'
# double_quoted_string = "Python Strings 8 O'clock"
# triple_quoted_string = '''Triple quotes allow "Python Strings 8 O'clock"
# strings to span multiple lines.'''
# print(single_quoted_string)
# print(double_quoted_string)
# print(triple_quoted_string)
# print(type(single_quoted_string))
# print(type(double_quoted_string))
# print(type(triple_quoted_string))



# sample = ""
# print(type(sample))


# sample_2 = str()
# print(type(sample_2))



# my_string = "Python"
#syntax
# var[index]
# print(my_string[0]) #P
# print(my_string[5]) #n
# print(my_string[-1]) #n
# print(my_string[3]) #h
# print(my_string[-3]) #h



# my_string = "Python"
#seq[s:s:s]
# print(my_string[1:5])#ytho
# print(my_string[-5:-1])#ytho
# print(my_string[4:0:-1])#ohty
# print(my_string[-2:-6:-1])#ohty


# name = "karthik" #htra
# print(name[4:0:-1])
# print(name[-3:-7:-1])



# user_name = "kalyanREDDY"
# upper_case = user_name.upper()
# print(upper_case)
# print(user_name)

# user_name = "kalyanREDDY@1234"
# upper_case = user_name.lower()
# print(upper_case)
# print(user_name)



# sentence = "This is a sample sentence."
# count_i = sentence.count('is')
# print(count_i) 

# whitespace_string = "   This is a string with leading and trailing whitespace.   "
# print(len(whitespace_string))
# stripped_string = whitespace_string.strip()

# print(len(stripped_string))

# sample = "python life"
# print(sample[7])



# data = "Pythonlife,Kiran,123456"
# data1 = data.split(',')
# print(data1)

# original_string = "Python is fun!"
# modified_string = original_string.replace('Python', 'pythonlife')
# print(modified_string)


# filename = "example.txt"
# starts_with = filename.startswith("ex")
# ends_with = filename.endswith(".txt")

# print(starts_with)  
# print(ends_with)  


# email_list = ["example1@gmail.com", "example2@yahoo.com", "example3@gmail.com", "example4@hotmail.com","example5@outlook.com"]
# empty_list = []
# for i in email_list:
#     if i.endswith("@gmail.com"):
#         empty_list.append(i)
# print(empty_list)

# sentence = "This is a sentence."
# position_a = sentence.find('z')
# position_i = sentence.index('z')

# print(position_a) 
# print(position_i) 

# text = "python programming"
# capitalized_text = text.capitalize()

# print(capitalized_text)


# numeric_string = "12345"
# alpha_string = "Python"
# is_numeric = numeric_string.isdigit()
# is_alpha = alpha_string.isalpha()
# print(is_numeric)  
# print(is_alpha)  


# word_list = ['Hello', 'World']
# joined_string = ' '.join(word_list)

# print(joined_string) 
# print(type(joined_string) )

# s = "python programming is fun"
# a = s.capitalize()
# print(a)


# s = "life"
# print(s[0:3])
# print(s[-4:-1])
# print(s[2::-1])
# print(s[-2::-1])


# l = [1,2,3,4,1,1,1,1,1,1,1]
# index = []
# for i in range(len(l)):
#     if l[i] == 1:
#         index.append(i)
# print(index)

# mul = int(input("enter"))
# for i in range(1,2):
#     for j in range(1,21):
#         print(f"{mul} X {j} = {mul*j}")

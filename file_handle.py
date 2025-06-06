# mode = 'r'
# file = open("demo.txt",mode = 'r')
# read_data = file.read()
# print(read_data)
# file.close()


# file = open("demo.txt",mode = 'r')
# read_data = file.readline()
# print(read_data)
# file.close()


# file = open("demo.txt",mode = 'r')
# read_data = file.readlines()
# print(read_data)
# file.close()

# read ---> total content return
# readline ---> single line return (first line)
# readlines --> file content list of substrings return( list of elements)



# mode = 'a' #append operations
# file = open("demo.txt",mode = 'a')
# write_data = file.write("performing write operations by using mode = 'a' ")
# file.close()


# file = open("sample123.txt", mode = 'a')
# file.close()


# mode = 'w' write operations and new file create
# file = open("demo.txt",mode = 'w')
# write_data = file.write("performing write  ")
# file.close() 

# voter_list = ["subbu\n","aravindh\n","vasu\n","kala\n","vignesh\n"]
# file = open("sample.txt", mode = 'w')
# write_data = file.writelines(voter_list)
# file.close()


# mode = 'w+' (all)
# file = open("sample.txt",mode = 'w+')
# write_data = file.write("this is file handling")
# print(file.tell())
# file.seek(0)
# read_data = file.read()
# print(read_data)
# file.close()


# mode = 'r'
# file = open("C:\\Users\\tarak\\Desktop\\pythonlife123.txt",mode = 'w')
# read_data = file.read()
# print(read_data)
# file.close()

# import os
# old_file = "demo.txt"
# new_file = "renamedemo.txt"
# os.rename(old_file,new_file)



# third party modules
# pypdf
# gtts

# import pypdf
# import gtts


# 1. find out the required module( dependencies )
# ---->  choose dedicated folder ( working directory )
# 2. create a virtual environment
# 3. activate the virtual environment
# 4. install the dependencies ( by using pip tool )
# 5. import the dependencies 
# 6. use the dependencies and complete the project


# import 
#syntax
# import modulename


# import functions1

#modulename.funcname()--> arguments within the parenthesis


# import functions1
# print(functions1.add(5,5))
# print(functions1.sub(5,5))
# print(functions1.expo(5,5))




# import conditionals




# from functions1 import *# * --->all
# print(add(5,5))
# print(sub(5,5))
# print(expo(5,5))


#built in functions
# import math
# print(math.sqrt(16))
# print(math.pi)
# print(math.pow(4,2))

# from math import *
# print(pi)
# print(pow(5,5))




# import random 
# from random import *
# print(randint(1,6))
# print(choice(['apple', 'banana', 'orange'])) 

# from datetime import datetime

# now = datetime.now()
# print(now)

# import os

# print(os.getcwd())

balance = 0

while True:
    print("\nATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        amount = float(input("Enter amount to credit: "))
        if amount <= 0:
            print("Please enter a positive amount.")
        else:
            balance += amount
            print(f"${amount} credited to your account.")
    elif choice == '2':
        amount = float(input("Enter amount to debit: "))
        if amount <= 0:
            print("Please enter a positive amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"${amount} debited from your account.")
    elif choice == '3':
        print(f"Your current balance is: ${balance}")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

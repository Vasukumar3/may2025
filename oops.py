#class syntax
# class classname():
#     #attr
#     #methods

# class details():#class definition
#     user_name = "arvindh" #attribute
#     id = 1234 #attribute
#     def details1(self): #methods
#         print("this is class method")
#         print(self.user_name)
#     def details2(self):
#         print("this is class method 2")
#         print(self.id)
#         self.details1()
# #object creation syntax 
# #objname = classname()
# obj = details()
# # obj.details1()
# # obj.details2()
# # print(obj.user_name)
# # print(obj.id)
# obj2 = details()
# obj2.details2()



# class mobiles(): #class definition
#     brand_name = "samsung" #attributes
#     color = "white"
#     storage = "128GB"
#     def calling(self,bn): #methods
#         print(f"you are calling.....{bn}")
#     def music(self):
#         print("you are listening...")
#     def browsing(self):
#         print("you are browsing...")
# #syntax
# # objname = classname()
# samsung = mobiles()
# samsung.calling("samsung")
# vivo = mobiles()
# vivo.calling("vivo")
# vivo.browsing()
# oppo = mobiles()
# oppo.music()




# class car():
#     def __init__(self,bn,color,model):
#         self.bn = bn
#         self.color = color
#         self.model = model
#     def driving(self):
#         print(f"you are driving {self.bn} ")
#     def engine(self,version):
#         print(f"start/off")
#         print(f"enging version {version} model {self.model}")
# tata = car("tata","white",2019)
# tata.driving()
# tata.engine("v8")
# mahindra = car("mahindra","black","2020")
# mahindra.driving()



# class featurephone():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def calling(self,number):
#         print(f"calling {number} from {self.brand} {self.model}")
#     def messages(self,number,message):
#         print(f"sending message {message} to {number} from {self.brand} {self.model} ")
# # samsung=featurephone("samsung",2015)
# # samsung.calling(1234567890)
# # samsung.messages(12345678,"hello everyone")
# class smartphone(featurephone):
#     def browsing(self):
#         print(f"bowsing internet on {self.brand} {self.model}")
#     def app(self,app_name,model):
#         print(f"using {app_name} app on {self.brand} {model}" )
# samsung= smartphone("samsung",2015)
# samsung.calling(123456789)
# samsung.messages(1234,"hii")
# samsung.browsing()
# samsung.app("spotify","s25ultra")




# class GrandFather:
#     def output(self):
#         print('this is gf class')
# class Father(GrandFather):
#     def outputf(self):
#         print('this is father class')
# class Child(Father):
#     def outputChild(self):
#         print('this is child class')  
# obj = Child()
# obj.output()
# obj.outputf()
# obj.outputChild()



# class a():
#     def parent(self):
#         print("this is parent class")
# class b(a):
#     def child1(self):
#         print("this is child 1 class")
# class c(a):
#     def child2(self):
#         print("this is child 2 class")

# obj = b()
# obj.parent()
# obj.child1()
# obj2= c()
# obj2.parent()
# obj2.child2()


# class parent1():
#     def father(self):
#         print("this is father class")
# class parent2():
#     def mother(self):
#         print("this is mother class")
# class child(parent1,parent2):
#     def child(self):
#         print("this is child class")
# obj = child()
# obj.father()
# obj.mother()
# obj.child()



# class atm():
#     def __int__(self,bn,location,balance):
#         self.bn = bn
#         pass
#     def withdraw(self):
#         pass
#     def credit(self):
#         pass
# class atm2(atm):
#     def balance(self):
#         pass
#     def exit(self):
#         pass
# class atm3(atm2):
#     def ministatement(self)








###################  may 22 2025 ###################

#polymorphism ---> implementing same thing in different forms
# 1.overloading --> 1. operator overloading 2. method overloading
# 2.method overriding 


#1. 1.operator overloading 
# ( + )
# a = 10
# b = 20
# print(a+b)


# a = "kiran"
# b = "raju"
# print(a+b)




# method overloading ---> 
# method name should be same
# arguments must be different ---> in the terms of length or type of arguments



# class calculator():
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# #objname = classname()
# obj = calculator()
# # obj.add(10,10)
# obj.add(5.5,5.7,2.5)


# method name should be same
# arguments must be different ---> in the terms of length or type of arguments
# class calculator():
#     def add(self,a=None,b=None,c=None):
#         print(a,b,c)
# obj = calculator()
# obj.add("vasu","kumar","pythonlife")
# obj.add(10,10,10)
# obj.add(10,"vasu",5.7)
# obj.add("vasu","kala","arvind")
# obj.add("vasu","kala")
# obj.add("vasu",)
# obj.add()












# 2.method overriding--> method name should be same, arguments should be also same
# class father():
#     def details(self,a):
#         print("this is base class",a)
# class child(father):
#     def details(self,a):
#         print("this is child class",a)
#         super().details(100)
# obj = child()
# obj.details("100cr")



# binding of class (methods and variables(attributes))
# # public 
# # and 
# # private __
# # protected _


# class Gfather():
#     def __init__(self,a):
#         self._a = a
#         print("gfather class",a)
# class Father(Gfather):
#     def display(self):
#         print(self._a)
# obj = Father("100cr")
# obj.display()





# class Gfather():
#     def __init__(self,a):
#         self.__a = a
#         print("gfather class",a)
# class Father(Gfather):
#     def display(self):
#         print(self.__a)
# obj = Father("100cr")
# obj.display()




#abstraction --> hiding the implementation and showing only essential part

# 1.abstract class --> class which contain abstract methods is called abstract class
# 2.abstract method --> the method which is having only declaration but not the definition is called abstract method (hiding the implementation)
# class which does not have abstract method is called concrete class
# concrete class  --> class without abstract methods
# object cannot create for abstract class
# object can create only concrete classes
# To create abstract classes in Python, you can use the abc (Abstract Base Classes) module

# from abc import ABC, abstractmethod
# class abstract_demo(ABC):
#     @abstractmethod
#     def display(self):
#         pass
#     @abstractmethod
#     def display2(self):
#         pass
# class demo(abstract_demo):
#     def display(self):
#         print("implementing in derived class")
#     def display2(self):
#         print("implementing derived class display 2")
# obj = demo()
# obj.display()
# obj.display2()



# from abc import ABC, abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def payment_processing(self):
#         pass

# class gpay(payment):
#     def payment_processing(self):
#         print("amount received from gpay..")
# class phonepe(payment):
#     def payment_processing(self):
#         print("amount received from phonepe...")



# complete BMS system by implement oops concept


#user login --> username and password
#


# import random
# print(random.randint(1111111111,99999999999))

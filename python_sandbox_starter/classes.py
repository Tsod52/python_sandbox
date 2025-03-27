# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#create a class

class User:
	#Constructor
	def __init__(self,name,email,age):
		self.name =name
		self.email = email
		self.age = age 

	def greeting(self):
		return f'My name is {self.name} and I am {self.age}'

	def has_birthday(self):
		self.age+=1

#Extend Class 
class Customer(User):
	def __init__(self,name,email,age):
		self.name =name
		self.email = email
		self.age = age 
		self.balance = 0

	def set_balance(self,balance):
		self.balance = balance

	def greeting(self):
		return f'My name is {self.name} and I am {self.age}. My balance is ${self.balance}'

#init user object 
albert = User('Albert Tsododo', 'at534@nyu.edu',21)
#init customer object
janet =Customer('Janet Manyowa','janet@gmail.com', 34)

albert.has_birthday()
print(albert.greeting())

janet.set_balance(2000)
print(janet.greeting())


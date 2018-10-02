class Person:
	def __init__(self,name,age,gender):
		self.name=name
		self.age=age
		self.gender=gender
	def display(self):
		print("Name: "+self.name+"\nAge:",self.age,"\nGender: "+self.gender)
name=input()
age=int(input())
gender=input()
p=Person(name,age,gender)
p.display()
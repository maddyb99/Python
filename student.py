class Student:
	def __init__(self,name,marks):
		self.name=name
		self.marks=marks
	def display(self):
		print("\n\nName: "+self.name+"\nMarks:",self.marks)
	def getmarks(self):
		return self.marks
s=[]
for i in range(0,9):
	name=input()
	marks=int(input())
	temp=Student(name,marks)
	s.append(temp);
for i in range(0,8):
	for j in range(i+1,9):
		if(s[i].getmarks()>s[j].getmarks()):
			temp=s[i]
			s[i]=s[j]
			s[j]=temp
for i in range(0,9):
	s[i].display()
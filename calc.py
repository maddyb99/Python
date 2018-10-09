class Calc:
	def add(self):
		return self.num1+self.num2
	def sub(self):
		return self.num1-self.num2
	def mul(self):
		return self.num1*self.num2
	def div(self):
		if(self.num2==0):
			return("Cannot Divide")
		return self.num1/self.num2
p=Calc()
setattr(Calc,"num1",int(input()))
setattr(Calc,"num2",int(input()))
print("1. Add\n2. Subtract\n3. Divide\n4. Multiply\n5. Exit")
opt=int(input())
if(opt==1):
	print(p.add())
elif(opt==2):
	print(p.sub())
elif(opt==3):
	print(p.div())
elif(opt==4):
	print(p.mul())
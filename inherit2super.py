class D():
	def __init__(self,f):	
		self.f=f
		print("D")
class B(D):
	def __init__(self,c,d):
		super().__init__(1)
		super().__init__(5)
		self.c=c
		self.d=d
		print("B")
class C(D):
	def __init__(self,e):
		super().__init__(2)		
		self.e=e
		print("C")
class A(B,C):
	def __init__(self,a,b):
		super().__init__(3,4)
		self.a=a
		self.b=b
		print("A")
a=A(6,7)
print(a.f)
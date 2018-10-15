class A:
	def __init__(self,a,b):
		super().__init__(3,4)
		self.a=a
		self.b=b
class B():
	def __init__(self,b,c):
		self.c=c
		self.d=b
class C(A,B):
	def __init__(self,a):
		super().__init__(1,2)
		self.e=a
c=C(5)
print(c.c)
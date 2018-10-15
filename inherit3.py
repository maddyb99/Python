class A():
	def __init__(self,a,b):
		self.a=a
		self.b=b
class B(A):
	def __init__(self,b,c):
		A.__init__(self,1,2)
		self.c=c
		self.d=b
class C(B):
	def __init__(self,a):
		B.__init__(self,3,4)		
		self.e=a
class F(B):
	def __init__(self,a):
		B.__init__(self,9,10)		
		self.h=a
class D(C,F):
	def __init__(self,a):
		C.__init__(self,5)	
		self.f=a
class E(D,A):
	def __init__(self,a):
		D.__init__(self,6)	
		A.__init__(self,7,8)
		self.g=a
a=E(11)
print(a.a)
class D():
	def __init__(self,f):	
		self.f=f
class B(D):
	def __init__(self,c,d):
		D.__init__(self,2)
		self.c=c
		self.d=d
class C(D):
	def __init__(self,e):
		D.__init__(self,1)		
		self.e=e
class A(B,C):
	def __init__(self,a,b):
		B.__init__(self,3,4)
		C.__init__(self,5)
		self.a=a
		self.b=b
a=A(6,7)
print(a.f)
class A:
	def __init__(self,a,b):
		super.__init__()
		self.a=a
		self.b=b
class B():
	def __init__(self,c,d):
		#super.__init__()
		self.c=c
		self.d=d
class C(A,B):
	def __init__(self,e):
		super.__init__(1,2)
		super.__init__(3,4)
		self.e=e
c=C(5)
print(c.c)
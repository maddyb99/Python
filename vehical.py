class Vehical:
	def __init__(self,company,color,typ,mile):
		self.company=company
		self.color=color
		self.milage=mile
		self.type=typ
	def display(self):
		print("Company: "+self.company+"\nColor:"+self.color+"\nType: "+self.type+"\nMilage: ",self.milage)
	def fuelcalc(self,km):
		fuel=km/self.milage
		print("fuel required=",fuel,"l")
company=input()
mileage=int(input())
typ=input()
color=input()
p=Vehical(company,color,typ,mileage)
p.display()
km=int(input())
p.fuelcalc(km)
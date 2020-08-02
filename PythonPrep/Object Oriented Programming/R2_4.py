class Flower:

	def __init__(self):
		name = ''
		petals = 0
		price = 0.0

	def updatename(self,a):
		self.name = a

	def getname(self):
		print (self.name)

	def updatepetals(self,a):
		self.petals = a

	def getpetals(self):
		print(self.petals)

	def updateprice(self,a):
		self.price = a

	def getprice(self):
		print (self.price)

a = Flower()
a.updatename('Rose')
a.updateprice(100.5)
a.updatepetals(10)
a.getname()
a.getprice()
a.getpetals()
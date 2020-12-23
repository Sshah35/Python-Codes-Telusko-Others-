class Computer:
	def __init__ (self) -> object:
		self.name="sam"
		self.age=30
	def update(self):
		self.name = 'Rick'
		self.age = 30
	def compare (self, comp2):

		if self.age == comp2.age:
			return True
		else:
			return False


comp1=Computer()
comp2=Computer()

comp1.name = 'Rajesh'
comp1.age= 30



if comp1.compare == (comp2):
	print( 'This is the same computer')
else:
	print('They have different age')


print(comp1.name , comp1.age)
print(comp2.name , comp2.age)

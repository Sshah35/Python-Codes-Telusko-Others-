class Car:
	wheels=2  # This is the class variable so this is going to be class nameSpace
	'''so the wheels is the class variable and it is also called the statice variable '''

	def __init__ (self):
		self.mile=5000  # so this are the instance variable instance namespace
		self.comp='BMW'


c1=Car()
c2=Car()

print(c1.mile , c1.comp , c1.wheels)
print(c2.mile , c2.comp , c2.wheels)

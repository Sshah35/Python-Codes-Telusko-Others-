class Computer:

	def __init__(self, cpu , ram ,size ):
		self.cpu  = cpu
		self.ram  = ram
		self.size = size
#		print('init')

	def config (self):
		print("Your choice of Computer : ", self.cpu, self.ram, self.size )

comp1=Computer('Del' , '16gb' , '1T ')

comp2=Computer('Hp', '32gb', '1T')

'''So we could use this one as well to call upon comp object'''
Computer.config(comp1)
Computer.config(comp2)

''' So we have one object of the class computer that is comp1 and we are usigng comp1.congig()
So this method is used mostly'''
comp1.config()
comp2.config()



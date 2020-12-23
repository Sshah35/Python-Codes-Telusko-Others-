class Computer:

	def config (self):
		print(" i5, 16gb, 1TB")

'''a='8'
print(type(a)) '''
comp1=Computer()
comp2=Computer()
# print(type(comp1))
Computer.config(comp1)
Computer.config(comp2)

comp1.config()
comp2.config()



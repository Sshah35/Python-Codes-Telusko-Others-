class A:
	def __init__ (self):
		print(' In A InIT')

	def feature1 (self):
		print('Feature1 is working')

	def feature2 (self):
		print('Feature2 is working')


class B():
	def __init__ (self):
#		super().__init__()  # so after creating this init method it will create this will call the init of A by creating the super()
		print(" in B Init")

	def feature3 (self):
		print('Feature3 is working')

	def feature4 (self):
		print("Feature4 is working")
class C(A,B):
	def __init__ (self):               # it will call only c method
		super().__init__()             # it will find A and C goes from A  and B left to right MRO concept 
		print(" in C Init")
#a1=A()
#a1=B()
a1=C()

# a1 = B()     # so this is the not possible If you don't create the init it will go up output:  In A InIT In A InIT

'''class constructor in inherritance topic of METHOD RESOLUTION ORDER or MRO'''

class A:
	def show(self):
		print('in A show')
class B(A):
#	pass
	def show(self):
		print('in b show')
a1 = B()
a1.show()
''' So when ther is no show method in the class B it inherits the show method from the class A
Now as soon as we create the show method in the class B it will overide the show method
from the class B and point to show the class method B from its own class 
Phone e.g Dad and Sun '''
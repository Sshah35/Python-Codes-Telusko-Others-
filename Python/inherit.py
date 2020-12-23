
class A :
	def feature1(self):
		print('Feature1 is working')
	def feature2(self):
		print('Feature2 is working')

class B(A):
	def feature3(self):
		print('Feature3 is working')
	def feature4(self):
		print('Feature4 is working')
class C(B):
	def feature5(self):
		print('Feature5 is working')
	def feature6(self):
		print('Feature6 is working')


a1 = A()
a1.feature1()
a1.feature2()
'''This is an example of the inherritance single Inherritance '''
b1 = B()
b1.feature3()
b1.feature4()
b1.feature1()
b1.feature2()
'''This is an example of the multilevel  inherritance 
Now if B is removed inherritance of A and C want to acess both the A and C 
class C(A,B):  Then this is called the multiple inherritance'''
c1 = C()
c1.feature1()




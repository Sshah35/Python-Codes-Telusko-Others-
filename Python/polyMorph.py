
###################Duck Typing we have ide pycharm and IDE editor as long as we have execute()
class PyCharm:
	def execute(self):
		print('compiling Pycharm')
		print('Running Pycharm')
class editor:
	def execute(self):
		print('spell check editor')
		print('conventional check editor')
		print('compiling editor ')
		print('Running editior')
class Laptop:
	def code(self, ide):
		ide.execute()
#ide = editor()
#print( 'So we are using the IDe Editor here ')
ide = PyCharm()
print ('Here we are uing the Pycharm editor')
lap1 = Laptop()
lap1.code(ide)

############################ operator overloading

class Student:
	def __init__(self,m1,m2):
		self.m1 = m1
		self.m2 = m2

	def __add__(self, other):
		m1 = self.m1 + other.m1
		m2 = self.m2 + other.m2
		s3 = Student(m1,m2)
		return s3
	def __gt__(self, other):
		s1 = self.m1 + self.m2
		s2 = other.m1 + other.m2
		if s1 > s2 :
			return True
		else:
			return False
# so this is the example how we could use or implement overload
	def sum (self,a=None,b=None,c=None):
		s=0
		if a!=None and b!=None and c!=None:
			s= a+b+c
		elif a!=None and b!=None:
			s= a+b
		else:
			s=a
		return s

s1 = Student(61,79)
s2 = Student(60,69)
s3 = s1 + s2

print(s3.m1)

print(s3.m2)

print(s1.sum(5), 'sum method overload')
######################### another example comparing students mark
if s1 > s2 :
	print('S1 Wins')
else:
	print('S2 wins')


'''Conept of poly morphism which means poly and morph one thing can take many forms
There are concepts in polymorphism like Loose Coupling, Dependency Injection,Interface
 There are 4 ways of implementing Polymorphism in Python
 Duck Typing | Operator Overloading | Method Overloading | Mehod Overriding
 In python there is no method overloading concept we have concept of *args
 or pass the null e.g a=none b= none c= none'''
#############################################################################################




class Student:

	def __init__ (self , name , id):
		self.name=name
		self.id=id
		self.lap=self.Laptop()

	# define out side object of the inner class

	def show (self):
		print(s1.name , s1.id)
		print(s2.name , s2.id)
		self.lap.show()


	class Laptop:

		def __int__ (self):
			self.brand='HP'
			self.cpu='i7'
			self.ram='8'

		def show (self):
			print(self.brand , self.cpu , self.ram)


s1=Student('navin' , 2)
s2=Student('Jenny' , 3)
# object of the inner class created and it is in the outer class
# s1.show()

'''lap1 = s1.lap
lap2 = s2.lap    # you can creat the object directly outside the class lap1 = Student.Laptop()

print (id (lap1))
print(id  (lap2))'''


#lap1=Student.Laptop()


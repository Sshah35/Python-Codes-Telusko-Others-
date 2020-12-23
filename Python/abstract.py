
from abc import ABC, abstractmethod

class Computer(ABC):

	@abstractmethod
	def process(self):
		pass

class Laptop(Computer):

	def process(self):
		print('Its is running Laptop')

class Whiteboard:

	def write(self):
		print( ' Writing on the whiteboard')

class Programmer:

	def work(self, com):
		print('solving Bugs')
		com.process()            # calling it from work commented our com1
#com = Computer()
#com.process()

com1 = Laptop()
com2 = Whiteboard()
#com1.process()

pro1 = Programmer()
pro1.work(com1)



'''In python does not support the Abstract but we could tweak 
Normal method have a head and body are in Normal classes 
 IF you only declare the method and not the body. we could create the method and then pass that is one way
  where there is no defination.
 another way is import abstact method and ABC module and use @Decorator and then instanstiate it to use
 ABC stands for Abstract Base Classes module 
 '''

from threading import *
from time import sleep
class Hello(Thread):


	def run(self):
		for i in range(5):
			print('Hello ')
			sleep(1)
class Hi(Thread):


	def run(self):
		for i in range(5):
			print('Hi ')
			sleep(1)
t1 = Hello ()
t2 = Hi ()

# t1.run()
# t2.run()
t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()
print('Bye')

''' Threads : application like MS word application has several subprocess and further breaking
this further to threads. each feactures that it  has can be broken down to seperate threads
 multiple core cpu we can run multiple applications , in game we have several events so many 
 things happening at the same time this will happen on multiple core
  Every execution had by default main thread 
  Now to implement  you must execute start method instead of run  Then use the sleep after import
  and also use gap to avoid collison
  To print the bye at end we need to use the join '''
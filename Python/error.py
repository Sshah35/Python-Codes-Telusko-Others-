
a = 5
b = 6

try:
	k=int(input('Enter the desired number: '))
	print(k)
	print('Resource opened ')
	print(a / b)
except	ZeroDivisionError as e:
	print ( " Hey, You cannot divide a Number by zero" , e)
except ValueError as e :
	print('Invalid Input please enter the valid input')
except Exception as e:
	print('Something went wrong Pleae try again')
finally:
	print("resouce closed Bye ")

''' Three type error 
Syntactical Error or Syntax Erro or Compile time error program will not execute
Logical Error programm will run with the wrong answer , Bugs during testing 
Run Time error execution error input error exception most important
User giving a wrong input error e.g zero or negative number or not entering string
try catch finally '''
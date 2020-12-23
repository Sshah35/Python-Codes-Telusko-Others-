
pos= -1
def search (list, n):
	i = 0
	while i < len(list):
		if list[i] == n:
			globals()['pos']= i
			return True
		i= i + 1
	return False

list = [55,4,6515,131,13,131,33131]

n= int(input('Please enter a number to searh if it is in a list : '))

if search (list, n):
	print("Found at index# :", pos+1,n)

else:
	print('Not Found')


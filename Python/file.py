
f= open('MyData.txt', 'r')   # to read the file
# print(f.readline())
f1= open('abc.txt' , 'a')       # to write the file if the file does not exist it will create the new file
# f1.write('\nThis is a new file')
# f1.write('\nThis is sam ' )
'''To store the file in a text file. open the data from the file the text file'''
for data in f:
	f1.write(data)
	
f1= open('abc.txt' , 'r')
print(f1.read())

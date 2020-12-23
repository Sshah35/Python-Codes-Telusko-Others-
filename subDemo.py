import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user = 'sam', passwd='Vidhi2013$', database= 'telusko')

mycursor = mydb.cursor()

#mycursor.execute("show databases")
mycursor.execute('select * from student')
#  here we are using cursor and the for loop directly to reterive data 
#for i in mycursor:
#	print(i)
# This for  loop we are creating the result  and storing all the records inside result 
#by using the fetchall() you could also use fetchone() to fetch only one record

#print('using the fetchall')
#result = mycursor.fetchall()

print('using the fetchone ')
result = mycursor.fetchone()

for i in result:
	print(i)


print('\nWelcome to sublime this is been eddited using the sublime')

print('\nThis is the sublime editor code that can be used to run the python scripts')

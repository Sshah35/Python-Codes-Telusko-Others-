
names = ('Nancy', 'Jessica', 'samantha', 'Nancy')
comp = ('Dell' , 'IBM', 'Google', 'yahoo')

emp= zip(names,comp)

print('\ncreating the list:')
empli = list(emp)
print(empli)

print('\nCreating the set: ')
set1 = set(zip(names,comp))
print (set1)

print('\ncreating a dictionary:')
dict1 = dict( zip(names,comp))
print(dict1)

print('\nNow using the itterator:')
zipped = zip(names,comp)

for (a,b) in zipped:
	print (a,b)


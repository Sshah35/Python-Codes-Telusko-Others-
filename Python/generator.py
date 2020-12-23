
def topten ():
	n=1
	while n <= 10:
		sq = n*n
		yield sq
		n = n+1
'''It is used to fetch data one by one instead of loading it to memory to all '''
	# yield 1
	# yield 2
	# yield 3
	# yield 4
	# yield 5

values = topten()
for i in values:
	print(i)
# print(values.__next__())
# print(values.__next__())
# for i in values:
# 	print(i)



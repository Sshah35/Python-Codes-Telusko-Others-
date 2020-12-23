pos = -1
def search (list1, n):
	low = 0
	upp = len(list1)-1
	while low <= upp :
		mid =  (low + upp) // 2

		if list1[mid] == n :
			globals()['pos'] = mid
			return True
		else:
			if list1 [mid] < n :
				low = mid +1
			else:
				upp = mid -1
	return False

list1 = [4,7,8,12,45,55,64,89,121,141,178,179]

n = int(input('Please enter a value to see if it is present: '))

if search (list1,n):
	print ("Found the number in list at position: ", pos+1)
else:
	print ('sorry not found in the list :')
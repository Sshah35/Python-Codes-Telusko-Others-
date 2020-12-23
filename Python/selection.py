def sort (nums):
	for i in range(len(nums)):
		minpos=i
		for j in range(i+1,len(nums)):
			if nums[minpos] > nums[j]:
				minpos =j
		nums[i], nums[minpos] = nums[minpos], nums[i]
		print(nums)


nums=[5 , 3 , 8 , 6 , 9 , 2 , 7 , 10]

sort(nums)
print(nums)

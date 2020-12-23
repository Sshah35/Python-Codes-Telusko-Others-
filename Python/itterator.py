
nums = [7,19,20,14,20,35,16,19,20]
class Topfive:
	def __init__(self):
		self.num = 1
	def __iter__(self):
		return self

#print(nums[5])
#for i in nums:
#	print(i, end=" ")
####### this is normal way to use the list
# it = iter(nums)
# print(it.__next__())
# print(it.__next__())
# print(next(it))

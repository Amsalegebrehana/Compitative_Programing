# # 424. Longest Repeating Character Replacement solution

def findMissing(nums):
		l=[]
		nums.sort()
		for i in range(nums[0], nums[len(nums)-1]+1):
			if i %2 !=0:
				l.append(i)
		for i in l:
			if i not in nums:
					return i
print( findMissing([1, 3, 5, 7, 9, 13, 15, 17]))
print( findMissing([9,3,7]))	
# from typing import Counter


# def findDifference(str):
#     dictt = Counter(str)
#     diff = abs(dictt['A'] - dictt['B'])
#     return diff
# print(findDifference("AABAAB"))
  
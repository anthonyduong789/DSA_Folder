"""
#Contains Duplicate
- solutions: use hash to detect and values are in array 
typically takes O(n)

"""


class Solution(object):
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		existingNumbers = {}
		
		for a in nums:
			if a not in existingNumbers:
				existingNumbers[a] = 1
			else:
				return True
		return False


	
	

        

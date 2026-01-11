"""
Insert Interval
- goal is to go ahead and find intersecting intervals

- if connecting intervals we simple merge
- if touching one but it extends it will change the interval min or max
- intervals are already sorted

conditions examples
if newInterval [l, r]

# if newInterval r is not in r interval and l is the one previous
	combine and the new interval r will max of preExisting and new one.

# if newInterval r is in r interval and l is the one previous
after that we check the next number if we get the max of the right interval and new interval.
	check condition again



hints/ other tips to try 
-use binary search 




"""

class Solution(object):
	def insert(self, intervals, newInterval):
		"""
		:type intervals: List[List[int]]
		:type newInterval: List[int]
		:rtype: List[List[int]]
		"""
		returnInterval = []
		i = 0

		while i < len(intervals):
			addInterval = []
			if newInterval[0] > intervals[i][0] and newInterval[0] < intervals[i][1]:
				addInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[0], intervals[i][1])]
				i+=1

				while(addInterval[1] >= newInterval[i][0]):
					addInterval = [addInterval[0], max(addInterval[1], newInterval[i][1])]
					i+=1
			if len(addInterval) != 0:
				returnInterval.append(addInterval)
			else:
				returnInterval.append(intervals[i])

			i+=1


		return returnInterval



				
				
				
			




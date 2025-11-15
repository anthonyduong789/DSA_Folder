"""
Greedy Method

example 1: loop through interval 

-if there is not an inteval that doesn't 
match pick that immediate interval

example 2: loop through interval 

can we have two paths that are taken if element is not removed?


-maybe we can have a hash for possible intevals that can be removed to remove the least amount

"""

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int

        bucket sort the first intevals by 1
        """

        # we start first with sorting intevals so we can iterate by the start
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            #checking for overlap
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)

        return res









leftmost
      
    


            

            





        


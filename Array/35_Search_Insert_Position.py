class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Going to similar to binary search 
        Insert where the elment in 

        right most elment > 
        left most elment <

        # edge cases
        # left most number
        # right most number

        """
        l = 0
        r = len(nums)

        if target > nums[r]:
            return r + 1
        if target < nums[l]:
            return 0

        while l < r:
            m = r - l // 2
            # case when the element is found 
            if nums[m] == target:
                return m
            if target < nums[m+1] and target > nums[m-1]:
                return m

            # case when the element is found 
            if target < nums[m]:
                r = m - 1
            if target > nums[m]:
                l = m + 1
        
        return 


"""
had missed the
r = m - 1
l = m + 1
"""
        
        
        

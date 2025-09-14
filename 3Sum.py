class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # position can't be the same
        # use a number x that we will lock in as our number we have 
        # subtract from the target we have which is 0
        # after that we have a 2 sum problem at hand 
        nums.sort()
        res = []


        for a in range(0, len(nums)):

            if a > 0 and nums[a] == nums[a-1]:
                continue
            l = a +1
            r = len(nums) - 1
            while l < r:
                tempSum = nums[l] + nums[r] + nums[a]

                if tempSum < 0:
                    l += 1 
                if tempSum > 0:
                    r -= 1 

                if tempSum == 0:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1

        return res







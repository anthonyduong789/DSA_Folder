class Solution(object):
    def neetCodeSolutions(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        i = 0 
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1

            i += 1



    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        ideas: maybe I can go ahead and have a way to shift the values l and r

        we sort the values and if the value has a value to the left of it that is the same
        we stop in that place

        ^same for going to the right better to start on ends? 
        what is the the point we know when to stop

        since we know that the values can only be 0, 1, 2
        the difference between l and r value can only be 
        that 1 if not then we definitely need to shift / move value


        have one pointer in the end 

        have the left pointer in the begginng
        if the nums[l] > nums[r]:
            switch value
        if same move pointer r to the left and check again

        if l and r == index reset r to the very right

        because we only have 3 value we can do this if element > 
        """
        l = 0
        r = len(nums)

        while l < len(nums):
            if nums[l] > nums[r]:
                new_left = nums[r]
                nums[r] = nums[l]
                nums[l] = new_left

            elif l == r:
                r = len(nums)
                l += 1
            

            elif nums[l] <= nums[r]:
                r -= 1

        return nums










    

     





        




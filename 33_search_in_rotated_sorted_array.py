class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        cases:
        when middle[] < r
        """
        l = 0 
        r = len(nums)

        while(l < r):
            m = (l + r) // 2
            # this shows that m -> is in ascending order
            if nums[m] == target:
                return m

            # this would also indicate that target < right because it's ascending
            elif nums[m] <= nums[r]:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

            # left is ascending right has rotary
            else:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m +1

        return -1





                

                        # we know left is has a rotary/ right is ascending



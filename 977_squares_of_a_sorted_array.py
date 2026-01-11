import heapq
from typing import MappingView

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        solution because we know that the the highest possible 
        amount when we square it are at left and the right
        we calc it and add it / change it for values r to left
        make a prequesting list to replace value


        """
        # ideas make a max heap where we put the elements squared allow then we pop the elements out
        # ouput is the same if the we sorted by abosulte value and then squared it
        l = 0
        r = len(nums)
        res = [0] * len(nums)
        placement = len(nums) - 1

        while(l <= r):
            left = nums[l] * nums[l]
            right = nums[r] * nums[r]

            if left < right:
                res[placement] = right
                r -= 1
            elif left > right:
                res[placement] = left
                l += 1
            else:
                # during ties we place right
                res[placement] = right
                r -= 1

            placement -= 1

        return res

            

                


            


            






























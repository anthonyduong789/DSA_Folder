from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        generate left and right side list that will save the product 
        of each index accumulation of multiplications
        """
        res = []
        left = []
        right = []

        #use 1 because of the identiy property for multiplication
        # [0, 1  3]
        leftStart = 1
        rightStart = 1

        for i in range(0, len(nums)):
            leftStart = leftStart * nums[i]
            left.append(leftStart)
            rightStart = rightStart * nums[len(nums) - 1 - i]
            right.append(rightStart)

        right.reverse()

        for i in range(0, len(nums)):
            leftProduct = 1
            rightProduct = 1
            if i != 0:
                leftProduct = left[i-1]
            if i != (len(nums) - 1):
                rightProduct = right[i+1]
            newNumber = leftProduct * rightProduct
            res.append(newNumber)

        return res

            
            
            





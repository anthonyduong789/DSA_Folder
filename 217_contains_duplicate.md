class Solution(object):
    <!-- Given an integer array nums, return true if any value appears at 
    least twice in the array, and 
    return false if every element is distinct. -->

    def containsDuplicates(self, nums):
        duplicates = set()

        for num in nums:
            if duplicates[num]:
                return True

            else:
                duplicates.add[num]

        return False
                
        
        


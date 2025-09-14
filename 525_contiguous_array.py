class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0 

        zeros = 0
        ones = 0
        # contains the difference from 0 and 1 at index i at the leftmost    element that contains it
        prefix = {}

        for index, num in enumerate(nums):
          if num == 0:
            zeros += 1
          else:
            ones += 1
          diff = zeros - ones
          
          
          if ones == zeros:
            current_length = index + 1
            
            if res < current_length:
              res = current_length


          if diff != 0:
            if diff not in prefix:
              prefix[diff] = index
            
            if diff in prefix:
              current_length = index - prefix[diff] 
            
              if res < current_length:
                res = current_length
          

        return res


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # we sort the values by the 1 digit having them largest ones in front
        for i, n in enumerate(nums):
          nums[i] = str(n)
        def compare(n1, n2):
          if n1 + n2 > n2 + n1:
            return -1
          else:
            return 1
          
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))


      

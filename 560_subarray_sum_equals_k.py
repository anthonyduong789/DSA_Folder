class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        curSum = 0
        prefixSum = {0: 1}
        for l in range(len(nums)):
            curSum += nums[l]
            neededPrefixSum = curSum - k
            res += prefixSum.get(neededPrefixSum, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        return res

    def subarraySum_BruteForce(self, nums, k):
        ret = 0
        for l in range(l, len(nums)):
            total = 0
            for r in range(r, len(nums)):
                total += nums[r]
                if total == k:
                    ret += 1
            
        return ret
    




if __name__ == "__main__":
    solutionObject = Solution()
    nums = [1,1,1]
    numberOfSubarrays = solutionObject.subarraySum(nums, 2)
    print(numberOfSubarrays)





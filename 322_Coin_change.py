from collections import deque


class Solution(object):
    """ "
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """

    """
    Approach 1: Brute-Force Recursion (Top-Down)
    The most direct way to translate our intuition is to use recursion. We define a function, let's call it solve(amount), that returns the minimum coins for that amount.

    Inside this function, we do the following:

    Base Cases:
    If amount is 0, we need 0 coins. Return 0.

    If amount is less than 0, it's an impossible situation (we overshot). Return -1 (or some other indicator of failure).

    Recursive Step:
    Initialize a variable min_coins to infinity.

    For each coin in our coins list:

    Recursively call solve(amount - coin).

    If the result of this call is not a failure, it means we found a valid combination. The total coins for this path would be 1 (for the current coin) plus the result.

    Update min_coins = min(min_coins, 1 + result).

    After checking all coins, if min_coins is still infinity, it means no solution was found. Otherwise, it holds our answer.

    This approach is correct, but it's very slow because it recalculates the solution for the same amount over and over again. For example, to get to amount = 11, both 11 -> 10 -> 5 and 11 -> 6 -> 5 will try to solve for amount = 5 independently.
    
    """

    def recursiveApproach(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        min_count = float("inf")
        for coin in coins:
            result = self.recursiveApproach(coins, amount - coin)
            if result != -1:
                min_count = min(min_count, 1 + result)

        return min_count if min_count != float("inf") else -1

        
    """
    Approach 2: Top-Down Dynamic Programming with Memoization
    To fix the repeated calculations from Approach 1, we can use a technique called memoization. It's just a fancy word for remembering the results of subproblems we've already solved.

    We'll use an array (or a map), let's call it memo, to store the answers. memo[i] will store the minimum coins needed for amount i.

    The logic is almost the same as before, with one crucial addition:

    Before calculating solve(amount), we first check if memo[amount] already has an answer.

    If it does, we just return that stored answer immediately without any further calculation.

    If it doesn't, we perform the calculation just like in Approach 1.

    Crucially, before returning the result, we store it in memo[amount] so we don't have to calculate it again later.

    This simple optimization dramatically improves the speed, as each subproblem is now solved only once.

    """
        
    def _approach2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.memo = {}
        return self._solve(coins, amount)
        
    def _solve(self, coins, rem):
        if rem < 0:
            return -1
        if rem == 0:
            return 0
        if rem in self.memo:
            return self.memo[rem]
        
        min_count = float('inf')
        
        for coin in coins:
            res = self._solve(coins, rem - coin)
            if res != -1:
                min_count = min(min_count, 1 + res)
        
        self.memo[rem] = min_count if min_count != float('inf') else -1
        return self.memo[rem] 
    
    
    
    
    
    

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        for this problem we can go ahead and
        for coin change what we can go ahead and do is we can have divide by current number
        and save amount that the number is the least least total amount of coins needed for that amount
        example
        ex/
        save the least amount of coins for 5
        """

        # dict will be least amount needed for 6
        leastCoinsNeededForx = {}
        for coin in coins:
            leastCoinsNeededForx[coin] = 1

        # maybe we can divide by largest amount then
        # see if amount in leastCoinsNeededForx then not manually try it?
        #
        #
        #

    def approach3(self, coins, amount):
        # made a mistake making list
        # dp = [[float('inf')] * amount* 1]
        #
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                # if coin <= i:
                if i - coin >= 0:
                    #compares current dp[i] with new possible combination
                    dp[i] = min(dp[i], 1+ dp[i-coin])

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
                    




class Solution(object):
    def gas_stations(self, gas, cost):
        """
        going to make a greedy alorithm where we pick the first gas 
        gas - cost

        greedy approach is going to be 
        O(N) 
        O(N) memory complexity
        """


        if sum(gas) < sum(cost):
            return - 1
        
        total = 0
        res = 0
         

        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            
            if total < 0:
                total = 0
                start = i + 1

        return res
                


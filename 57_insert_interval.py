class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]

        res = []
        newInterval = intervals[0]

        for i in range(1, len(intervals)):
            #this indicates a overlapping interval
            if newInterval[1] > intervals[i][0]:
                newInterval[1] = max(intervals[i][1], newInterval[1])
            else:

                res.append(newInterval)
                newInterval = intervals[i]


        # append the last interval left
        res.append(newInterval)

        return res





        
        


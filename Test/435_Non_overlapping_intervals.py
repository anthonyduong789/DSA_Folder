class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        sortIntervals = intervals.sort()
        prevEnd = intervals[0][1]
        removedIntervals = 0

        for start, end in intervals[1:]:
            currentInterval = intervals[i]
            # case 1 is there is going to be a overlap
            if start < prevEnd:
                removedIntervals += 1
                prevEnd = min(end, prevEnd)
            else: 
                prevEnd = end

            #case 2 is there is no overlap

        return removedIntervals








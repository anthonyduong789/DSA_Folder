
from typing import List


class Solution(object):
    def combinationSum(self, candidates, target):

        res = []
        def path_finder(path: List, index: int ,sum: int):
            
            # in this case the path is invalidated/ dead end stop going down this path
            if (sum > target):
                return
            if sum == target:
                res.append(path[:])

            # start from index to reduce different permutations of same values 
            for i in range(index, len(candidates)):
                # very important or the new Path can have multiple values sharing the same memory space
                newPath = path[:]
                newPath.append(candidates[i])
                newSum = sum + candidates[i]
                path_finder(newPath, i, newSum)



        path_finder([], 0, 0)


        return res


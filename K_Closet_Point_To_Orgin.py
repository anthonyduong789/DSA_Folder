"""
Ideas?

use a min queue that keeps track of the 
min amount closest to the orgin going through it 

^scratch this idea and we will go ahead and use a BST search tree and 
to a inOrder Traversal



if the queue return where the min orgin is to x elements
if points are the same this will alwasys prioritize the ones that came first

"""
import heapq  

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y + 2)
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k-=1
        
        return res

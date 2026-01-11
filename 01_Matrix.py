"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
-ideas 
- save the distance for each position i.e for [0,0] save the nearest distance from that block to the nearest 0
that we we don't have to consistenly keep doing it

- es similare to a flood fill ALGORITHM except if position we already have 
cross then we can go ahead and just reuse it 

- keep in mind breadth first search/ depth first search
^how to keep track of the depth/ distance from the intial start?
jk;steps:
solve using flood fill without the backtracking
then implement for time efficiency


THRIIIW
"""

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # this will find the nearsest 0 closest to this position using a flood
        # left top right,
        rows, cols = len(mat), len(mat[0])
        queue = []

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] != 0:
                     mat[i][j] = float('inf')
                else:
                    queue.append((i,j))
                    
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c = queue.pop(0)
            
            for dx, dy in directions:
                x, y = r+dx, c + dy
                if 0 <= x <rows and 0<= y < cols and mat[x][y] > mat[r][c] + 1:
                    mat[x][y] = mat[r][c] + 1
                    queue.append((x, y))
                        
        print(mat)
        return mat

def main():
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    solution = Solution()
    solution.updateMatrix(mat)

if __name__ == "__main__":
    main()






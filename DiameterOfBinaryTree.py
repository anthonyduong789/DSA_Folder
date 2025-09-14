# Definition for a binary tree node.
from typing import Optional

# NOTE: 
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        #return height

        def dfs(curr):

            if curr:
                print(curr.val)
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)



            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        dfs(root)

        return self.res
# Helper function to build a binary tree from a list
def build_tree(index, nodes):
    if index >= len(nodes) or nodes[index] is None:
        return None
    root = TreeNode(nodes[index])
    root.left = build_tree(2 * index + 1, nodes)
    root.right = build_tree(2 * index + 2, nodes)
    return root


def main():
    test1 = [1, 2, 3, 4, 5]
    root = build_tree(0, test1)

    sol = Solution()
    diameter = sol.diameterOfBinaryTree(root)
    print("Diameter of the binary tree:", diameter)
    



if __name__ == "__main__":
    main()









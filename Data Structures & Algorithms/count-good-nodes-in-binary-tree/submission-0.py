# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,maxi):
            res=0
            if root is None:
                return 0
            if root.val>=maxi:
                res=1
                maxi=root.val
            res+=dfs(root.left,maxi)
            res+=dfs(root.right,maxi)

            return res
        return dfs(root,float('-inf'))
        
        
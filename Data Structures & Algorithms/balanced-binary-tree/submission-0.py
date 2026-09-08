# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        x=0
        def height(root):
            nonlocal x
            if root is None:
                return 0
            left=height(root.left)
            right=height(root.right)
            diff=abs(left-right)
            if diff>1:
                x=1

            return 1+max(left,right)
        height(root)
        if x==0 :
            return True
        else:
            return False
        
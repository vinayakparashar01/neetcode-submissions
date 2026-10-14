# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(x,lists):
            if x is None:
                lists.append('#')
                return
            
            lists.append(str(x.val))
            dfs(x.left,lists)
            dfs(x.right,lists)
        result=[]
        y=dfs(root,result)
        root_str = "".join(result)
        roots=[]
        z=dfs(subRoot,roots)
        subroot_str = "".join(roots)
        return subroot_str in root_str


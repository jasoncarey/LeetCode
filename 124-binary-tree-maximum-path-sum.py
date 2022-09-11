# Binary Tree Maximum Path Sum
# ----------
# Hard
# Tree, DFS

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # declare global variable
        res = [root.val]
        
        def dfs(root):
            if not root: return 0
        
            # max ( , 0) handles negative node case
            # ie, if we have a negative path, ignore those children
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)
        
            # compute max WITH split (ie. we take both the left and right subtrees, and ignore parent nodes)
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            # return max WITHOUT split (ie. only take one left or right subtree)
            return (root.val + max(leftMax, rightMax))
        
        dfs(root)
        return res[0]
            
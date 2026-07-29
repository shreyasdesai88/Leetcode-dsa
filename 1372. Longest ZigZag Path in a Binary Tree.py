# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_path = 0
        
        def dfs(node):
            if not node:
                return -1, -1  # Returns (left_length, right_length)
            
            # Recurse on left and right subtrees
            _, left_right = dfs(node.left)
            right_left, _ = dfs(node.right)
            
            # Calculate zigzag lengths from the current node
            current_left = 1 + left_right
            current_right = 1 + right_left
            
            # Update the global maximum length found so far
            self.max_path = max(self.max_path, current_left, current_right)
            
            return current_left, current_right

        dfs(root)
        return self.max_path

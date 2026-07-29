# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        # Hash map to store: {prefix_sum : count_of_occurrences}
        # Initialize with {0: 1} to handle paths that match targetSum starting right from the root
        prefix_sums = {0: 1}
        
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Update the running sum from the root to this node
            current_sum += node.val
            
            # Check if there is a prefix sum that satisfies: current_sum - targetSum
            # If it exists, it means a valid sub-path sums up to targetSum
            valid_paths = prefix_sums.get(current_sum - targetSum, 0)
            
            # Add the current prefix sum to the hash map for deeper children nodes
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
            # Recursively count paths in the left and right subtrees
            valid_paths += dfs(node.left, current_sum)
            valid_paths += dfs(node.right, current_sum)
            
            # Backtrack: Remove the current sum from the map before moving back up the tree
            prefix_sums[current_sum] -= 1
            
            return valid_paths

        return dfs(root, 0)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob_prev1 = 0  
        rob_prev2 = 0  
        
        for num in nums:
            # Decide to either rob current house + two houses ago, or skip current house
            current_max = max(num + rob_prev2, rob_prev1)
            
            # Slide the variables forward for the next iteration
            rob_prev2 = rob_prev1
            rob_prev1 = current_max
            
        return rob_prev1

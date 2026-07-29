class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Handle small base cases directly
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
            
        # Initialize variables for the DP state transitions
        # f0, f1, f2 represent F(i-3), F(i-2), F(i-1)
        f0, f1, f2 = 1, 2, 5
        
        # Iteratively calculate the values up to n
        for i in range(4, n + 1):
            f_current = (2 * f2 + f0) % MOD
            f0, f1, f2 = f1, f2, f_current
            
        return f2

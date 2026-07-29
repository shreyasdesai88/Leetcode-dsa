import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # Define the boundaries of the binary search range
        low = 1
        high = max(piles)
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            
            # Calculate total hours needed at speed 'mid'
            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(float(pile) / mid)
                
            # If Koko finishes in time, try a slower speed
            if hours_spent <= h:
                result = mid
                high = mid - 1
            # If Koko takes too long, increase the speed
            else:
                low = mid + 1
                
        return int(result)

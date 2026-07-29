import bisect

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        # Sort potions to enable binary search
        potions.sort()
        m = len(potions)
        pairs = []
        
        for spell in spells:
            # Calculate the minimum required potion strength
            # Equivalent to ceil(success / spell) using integer arithmetic
            min_potion_needed = (success + spell - 1) // spell
            
            # Find the first index where potion >= min_potion_needed
            idx = bisect.bisect_left(potions, min_potion_needed)
            
            # All potions from idx to the end of the array are successful
            pairs.append(m - idx)
            
        return pairs

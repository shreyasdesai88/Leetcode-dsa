class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the next element is greater, the peak lies to the right
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # Otherwise, the peak lies to the left (including mid)
            else:
                right = mid
                
        return left

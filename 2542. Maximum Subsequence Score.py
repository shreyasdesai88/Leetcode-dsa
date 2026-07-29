import heapq

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        # 1. Pair elements together and sort by nums2 in descending order
        pairs = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
        
        min_heap = []
        current_sum = 0
        max_score = 0
        
        # 2. Iterate through the sorted pairs
        for num1, num2 in pairs:
            # Add current num1 to our active pool
            heapq.heappush(min_heap, num1)
            current_sum += num1
            
            # If our pool exceeds size k, remove the smallest element
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)
            
            # When we have exactly k elements, calculate potential max score
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * num2)
                
        return max_score

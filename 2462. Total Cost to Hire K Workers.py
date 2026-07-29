import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        # Min-heaps to store the available candidates
        left_heap = []
        right_heap = []
        
        left = 0
        right = len(costs) - 1
        
        total_cost = 0
        
        # Fill the heaps up to 'candidates' size, ensuring pointers do not cross
        while left < candidates:
            heapq.heappush(left_heap, costs[left])
            left += 1
            
        while right >= len(costs) - candidates and right >= left:
            heapq.heappush(right_heap, costs[right])
            right -= 1
            
        # Hire exactly k workers
        for _ in range(k):
            # Check tops of both heaps
            val1 = left_heap[0] if left_heap else float('inf')
            val2 = right_heap[0] if right_heap else float('inf')
            
            # Tie-breaker goes to left heap (smaller index)
            if val1 <= val2:
                total_cost += heapq.heappop(left_heap)
                # If there are still workers left, add to the left heap
                if left <= right:
                    heapq.heappush(left_heap, costs[left])
                    left += 1
            else:
                total_cost += heapq.heappop(right_heap)
                # If there are still workers left, add to the right heap
                if left <= right:
                    heapq.heappush(right_heap, costs[right])
                    right -= 1
                    
        return total_cost

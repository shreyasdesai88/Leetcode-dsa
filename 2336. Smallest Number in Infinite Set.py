import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        # Tracks the smallest number that hasn't been popped yet
        self.thres = 1
        # Min-heap to track numbers that were popped and added back
        self.added_heap = []
        # Hash set to prevent adding duplicate numbers to the heap
        self.added_set = set()

    def popSmallest(self):
        """
        :rtype: int
        """
        # If there are elements added back, the smallest must be in the heap
        if self.added_heap:
            smallest = heapq.heappop(self.added_heap)
            self.added_set.remove(smallest)
            return smallest
        
        # Otherwise, the smallest is the current threshold
        smallest = self.thres
        self.thres += 1
        return smallest

    def addBack(self, num):
        """
        :type num: int
        :rtype: none
        """
        # Only add back if it's smaller than the threshold and not already added back
        if num < self.thres and num not in self.added_set:
            heapq.heappush(self.added_heap, num)
            self.added_set.add(num)

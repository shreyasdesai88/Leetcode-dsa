from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Step 1: Find all initial rotten oranges and count fresh ones
        for r in xrange(rows):
            for c in xrange(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        # If no fresh oranges exist initially, 0 minutes are needed
        if fresh_count == 0:
            return 0
            
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Step 2: Spread the rot minute by minute using BFS
        while queue and fresh_count > 0:
            minutes += 1
            # Process all oranges that rotted in the previous minute
            for _ in xrange(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # If neighbor is within bounds and is a fresh orange
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Mark as rotten
                        fresh_count -= 1
                        queue.append((nr, nc))
                        
        # Step 3: If fresh oranges remain untouched, return -1
        return minutes if fresh_count == 0 else -1

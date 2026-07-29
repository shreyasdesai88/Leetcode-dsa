from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        start_row, start_col = entrance
        
        # Initialize queue with (row, col, current_steps)
        queue = deque([(start_row, start_col, 0)])
        
        # Mark the entrance as visited so we don't return to it
        maze[start_row][start_col] = '+'
        
        # Direction vectors for moving Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, steps = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check if the neighbor is inside the maze bounds and is an empty path
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    
                    # Check if this empty path sits on any boundary edge
                    if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                        return steps + 1
                    
                    # Mark as visited and add to queue to search deeper
                    maze[nr][nc] = '+'
                    queue.append((nr, nc, steps + 1))
                    
        return -1

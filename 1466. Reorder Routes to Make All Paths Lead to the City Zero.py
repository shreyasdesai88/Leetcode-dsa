from collections import defaultdict, deque

class Solution(object):
    def minReorder(self, n, connections):
        # Build an adjacency list for an undirected graph
        # Track the direction: 1 for original direction, 0 for artificial reverse direction
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append((v, 1))  # Original road u -> v
            adj[v].append((u, 0))  # Reverse road v -> u

        # BFS initialization
        queue = deque([0])
        visited = {0}
        change_count = 0

        while queue:
            curr = queue.popleft()
            
            for neighbor, direction in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # If direction is 1, it means the original road points away from 0 (curr -> neighbor)
                    # We must reverse it to point toward 0 (neighbor -> curr)
                    change_count += direction
                    queue.append(neighbor)

        return change_count

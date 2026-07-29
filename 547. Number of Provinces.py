class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        
        def dfs(node):
            for neighbor in range(n):
                # If there is a connection and the neighbor hasn't been visited yet
                if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
                    
        for i in range(n):
            if not visited[i]:
                provinces += 1
                visited[i] = True
                dfs(i)
                
        return provinces

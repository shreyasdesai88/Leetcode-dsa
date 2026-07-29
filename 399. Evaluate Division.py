from collections import defaultdict


class Solution(object):

    def calcEquation(self, equations, values, queries):
        # Step 1: Build the graph
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val

        # Step 2: Define DFS traversal to find path product
        def dfs(start, end, visited):
            # If the target is found, return 1.0 (base multiplier)
            if start == end:
                return 1.0

            visited.add(start)

            # Traverse neighbors
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    product = dfs(neighbor, end, visited)
                    # If a valid path is found, accumulate the weight
                    if product != -1.0:
                        return weight * product

            return -1.0

        # Step 3: Process each query
        results = []
        for u, v in queries:
            # If either variable has never been seen, it is undefined
            if u not in graph or v not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(u, v, set()))

        return results

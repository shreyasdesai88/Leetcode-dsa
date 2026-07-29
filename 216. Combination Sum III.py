class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        
        def backtrack(remain_sum, current_comb, start_num):
            
            if len(current_comb) == k and remain_sum == 0:
                results.append(list(current_comb))
                return
            
            
            if len(current_comb) > k or remain_sum < 0:
                return
            
            
            for i in range(start_num, 10):
                
                
                if i > remain_sum:
                    break
                    
                
                current_comb.append(i)
                
                
                backtrack(remain_sum - i, current_comb, i + 1)
                
                
                current_comb.pop()

        backtrack(n, [], 1)
        return results

        

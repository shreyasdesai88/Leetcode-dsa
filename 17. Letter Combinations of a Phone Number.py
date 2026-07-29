class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Return empty list if input is empty
        if not digits:
            return []
            
        # Telephone keypad mapping
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, current_combination):
            # Base case: if the combination is complete
            if len(current_combination) == len(digits):
                result.append("".join(current_combination))
                return
            
            # Get letters matching the current digit
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # Explore each letter option
            for letter in letters:
                current_combination.append(letter)  # Choose
                backtrack(index + 1, current_combination)  # Explore next digit
                current_combination.pop()  # Backtrack / Unchoose

        # Start recursion from index 0 with an empty combination list
        backtrack(0, [])
        return result

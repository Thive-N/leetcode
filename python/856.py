class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0] 

        for parentheses in s:
            if parentheses == "(":
                stack.append(0)
            elif stack:
                last_score = stack.pop() 
                stack[-1] += max(1, last_score * 2)
        
        return stack[-1]
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == "(":
                stack.append(")")
                continue
            elif x == "[":
                stack.append("]")
                continue
            elif x == "{":
                stack.append("}")
                continue
            y = 0
            try:
                y = stack.pop(-1)
            except:
                return False
            
            if x != y:
                return False

        if len(stack) != 0: 
            return False
        
        return True
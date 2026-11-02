class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in pairs:                        # c is a closer
                if not stack or stack.pop() != pairs[c]:
                    return False                  # empty stack or wrong opener
            else:                                 # c is an opener
                stack.append(c)
        return not stack    
        
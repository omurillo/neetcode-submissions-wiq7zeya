class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) % 2 != 0:
            return False

        stack = []
        for v in s:
            if v in "[({":
                stack.append(v)
            else:
                if len(stack) == 0:
                    return False
                openBracket = stack.pop()
                if v == ']' and openBracket == '[':
                    continue
                elif v == ')' and openBracket == '(':
                    continue
                elif v == '}' and openBracket ==  '{':
                    continue
                else:
                    return False
        return len(stack) == 0





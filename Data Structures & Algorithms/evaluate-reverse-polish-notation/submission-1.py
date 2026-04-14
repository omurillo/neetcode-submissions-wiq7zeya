class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["+", "-", "*", "/"])
        stack = []
        for val in tokens:
            if val in operators:
                b = int(stack.pop())
                a = int(stack.pop())
                if val == "+":
                    stack.append(a + b)
                elif val == "-":
                    stack.append(a - b)
                elif val == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(val)
        return int(stack[-1])


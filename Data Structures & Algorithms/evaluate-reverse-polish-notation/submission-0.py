class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in {'+', '-', '*', '/'}:
                b = stack.pop()  # right operand
                a = stack.pop()  # left operand
                if i == '+': stack.append(a + b)
                elif i == '-': stack.append(a - b)
                elif i == '*': stack.append(a * b)
                elif i == '/': stack.append(int(a / b))  # truncate toward zero
            else:
                stack.append(int(i))
        return stack[-1]
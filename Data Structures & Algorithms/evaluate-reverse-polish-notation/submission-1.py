class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = ['+','-','*','/']
        stack = []
        for i in range(0,len(tokens)):
            if tokens[i] not in symbols:
                stack.append(int(tokens[i]))
            else:
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == '+':
                    stack.append(a+b)
                elif tokens[i] == '-':
                    stack.append(a-b)
                elif tokens[i] == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack[0]

            
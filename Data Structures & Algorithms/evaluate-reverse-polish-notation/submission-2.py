class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            print(stack)
            if x=='+':
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num1+num2)
            elif x=='*':
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num1*num2)
            elif x=='-':
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num2-num1)
            elif x=='/':
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num2/num1)
            else:
                stack.append(x)
        return int(stack[0])
            
        
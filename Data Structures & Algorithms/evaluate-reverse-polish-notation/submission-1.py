class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        dmas = ["-","+","/","*"]

        for i in tokens:
            if i in dmas:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if i == "-":
                    res = num2 - num1
                elif i == "+":
                    res = num2 + num1
                elif i == "*":
                    res = num2 * num1
                elif i == "/":
                    res = num2 / num1

                stack.append(res)
            else:
                stack.append(i)

        return int(stack[0])
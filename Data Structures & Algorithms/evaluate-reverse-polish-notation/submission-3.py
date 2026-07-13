class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in "+-/*":
                x=int(i)
                stack.append(x)
            else:
                a=stack.pop()
                b=stack.pop()
                if i == "+":
                    c = b + a
                elif i == "-":
                    c = b - a
                elif i == "*":
                    c = a * b
                elif i == "/":
                    c = int(b / a)
                stack.append(c)
        return stack.pop()
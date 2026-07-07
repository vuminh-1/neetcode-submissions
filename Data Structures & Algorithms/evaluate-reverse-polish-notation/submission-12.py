class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def number(n:str):
            try:
                n = int(n)
                return True
            except ValueError:
                return False

        stk = []
        a: int
        b: int
        for i in range(len(tokens)):
            if number(tokens[i]):
                stk.append(int(tokens[i]))
            else:
                if tokens[i] == '+':
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(a + b)
                elif tokens[i] == '-':
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(b - a)
                elif tokens[i] == '*':
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(a * b)
                elif tokens[i] == '/':
                    a = stk.pop()
                    b = stk.pop()
                    stk.append(int(b / a))

        return round(stk[0])







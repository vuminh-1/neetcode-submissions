class Solution:
    def isValid(self, s: str) -> bool:
        def level(s):
            if s == '}' or s == '{':
                return 4
            elif s == ']' or s == '[':
                return 3
            elif s == ')' or s == '(':
                return 2
            else:
                return 1


        stk = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stk.append(i)
            elif (i == ')' or i == ']' or i == '}') and stk != []:
                if level(stk[-1]) ==  level(i):
                    del stk[-1]
                else:
                    return False
            elif i == ')' or i == ']' or i == '}' and len(stk) == 0:
                return False
        if stk != []:
            return False
        else:
            return True

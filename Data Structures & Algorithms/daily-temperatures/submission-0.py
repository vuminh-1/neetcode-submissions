class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stk = []
        for i in range(len(temperatures)):
            if stk == []:
                stk.append(i)
            else:
                if temperatures[i] > temperatures[stk[-1]]:
                    while temperatures[i] > temperatures[stk[-1]]:
                        res[stk[-1]] = i - stk[-1]
                        del stk[-1]
                        if stk == []:
                            break
                    
                    stk.append(i)
                else:
                    stk.append(i)
        return res



class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = {}
        for i in range(len(position)):
            pos[position[i]] = speed[i]
        p = sorted(pos.items())
        
        stk = []
        for i in range(len(position)):
            if stk == []:
                stk.append(i)
            else:
                if p[i][1] >= p[stk[-1]][1]:
                    stk.append(i)
                else:
                    while p[i][1] < p[stk[-1]][1]:
                        target = float(target)
                        time = (p[i][0] - p[stk[-1]][0]) / (p[stk[-1]][1] - p[i][1])
                        destination = p[i][0] + p[i][1]*time
                        if destination <= target:
                            stk.pop()
                            if stk == []:
                                break
                            else:
                                continue
                        else:
                            break
                    stk.append(i)
            
        return len(stk)



        

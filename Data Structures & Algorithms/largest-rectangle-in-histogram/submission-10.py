class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
            stki = []
            stkh = []
            max_area = 0
            for i in range(len(heights)):
                if stki == [] and stkh == []:
                    stkh.append(heights[i])
                    stki.append(i)
                elif heights[i] < stkh[-1]:
                    temp = 0
                    while heights[i] < stkh[-1]:
                        temp = stki[-1]
                        area = stkh[-1]*(i-stki[-1])
                        max_area = max(max_area,area)
                        stkh.pop()
                        stki.pop()
                        if stkh == []:
                            break
                    
                    stki.append(temp)
                    stkh.append(heights[i])
                    
                else:

                    stki.append(i)
                    stkh.append(heights[i])
            print(stki,stkh)
            for i in range(len(stkh)):
                area = stkh[i]*(len(heights) - stki[i])
                max_area = max(area,max_area)
            
            return max_area

                    



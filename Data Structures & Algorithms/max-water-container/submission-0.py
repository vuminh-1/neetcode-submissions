class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights) - 1):
            for j in range(i+1,len(heights)):
                if heights[j] > heights[i]:
                    area = heights[i] * (j - i)
                    max_area = max(area,max_area)

                elif heights[j] < heights[i]:
                    area = heights[j] * (j - i)
                    max_area = max(area,max_area)

                else:
                    area = heights[i] * (j - i)
                    max_area = max(area,max_area)
        return max_area
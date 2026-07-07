class Solution:
    def trap(self, height: List[int]) -> int:
        temp = height[len(height)-2]
        height.insert(0,0)
        height.append(temp)
        col = [0] * len(height)


        for i in range(1,len(height)-1):
            if height[i-1] <= height[i] and height[i+1] <= height[i]:
                col[i] = 1
        
        for i in range(len(height)-1):
            if col[i] == 1:
                max_col = 0
                id_of_max = 0
                for j in range(i+1,len(height)):
                    if col[j] == 1 and height[j] >= height[i]:
                        if height[j] > max_col:
                            max_col = height[j]
                            id_of_max = j
                    
                        break

                for k in range(i+1,id_of_max):
                    col[k] = 0 

        for i in range(len(height)-1):
            if col[i] == 1:
                for j in range(i+1,len(height)):
                    if col[j] == 1:
                        for k in range(i+1,j):
                            if height[k] > height[j]:
                                col[k-1] = 0
                                col[k] = 1
                        break
                    else:
                        pass
    
        area = 0 
        for i in range(len(height)-1):
            if col[i] == 1:
                for j in range(i+1,len(height)):
                    if col[j] == 1:
                        if height[i] < height[j]:
                            area += height[i] * (j - i + 1) - sum(height[i+1:j]) - 2*height[i]
                        else:
                            area += height[j] * (j - i + 1) - sum(height[i+1:j]) - 2*height[j]
                        break
            else:
                pass
            
        return area
            

        
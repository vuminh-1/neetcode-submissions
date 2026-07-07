class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0 
        r = l + k - 1
        res = []
        temp = 0
        indice = 0
        for i in range(l,r+1):
            if temp < nums[i]:
                temp = nums[i]
                indice = i
        r += 1
        l += 1
        res.append(temp)
        while r < len(nums):
            if indice in range(l,r+1):
                if temp < nums[r]:
                    temp = nums[r]
                    res.append(temp)
                    indice = r 
                else:
                    res.append(temp)
            else:
                if temp < nums[r]:
                    temp = nums[r]
                    res.append(temp)
                    indice = r
                else:
                    temp = max(nums[l:r+1])
                    for i in range(l,r+1):
                        if nums[i] >= temp:
                            temp = nums[i]
                            indice = i
                    res.append(temp)
            l += 1
            r += 1
        
        return res

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) > 0:
            if min(nums) < 0:
                check = [0]*(max(nums) - min(nums) + 1)
            else:
                check = [0]*(max(nums)+1)
        else:
            return 0
        
        if min(nums) < 0:
            for i in nums:
                if i == 0:
                    check[abs(min(nums))] = 1
                elif i < 0:
                    d = abs(min(nums)) - abs(i)
                    check[d] = 1
                elif i > 0:
                    d = abs(min(nums)) + i
                    check[d] = 1
        else:
            try:
                for i in nums:
                    check[i] = 1
            except IndexError:
                print(i)
            
        #main job
        long = 0
        maxi = 0
        for i in check:
            if i == 1:
                long += 1
            else:
                if maxi < long:
                    maxi = long
                long = 0 
        if maxi < long:
            maxi = long

        return maxi



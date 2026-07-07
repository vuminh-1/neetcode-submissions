class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def check(a,m):
            a.sort()
            m.sort()
            if a == m:
                return True
            else:
                return False
        
        def check2(a,m):
            for i in m:
                if check(a,i):
                    return False
                else:
                    continue
            
            return True



        res = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if check2([nums[i],nums[j],nums[k]],res):
                            res.append([nums[i],nums[j],nums[k]])

        return res
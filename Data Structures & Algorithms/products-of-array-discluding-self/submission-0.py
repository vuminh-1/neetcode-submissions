class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = [1]
        for i in range(1,len(nums)):
            a.append(nums[i-1] * a[i-1])
        
        b = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            b[i] = b[i+1] * nums[i+1]
            
        res = []
        for j in range(len(b)):
            res.append(b[j]*a[j])
        return res
















        
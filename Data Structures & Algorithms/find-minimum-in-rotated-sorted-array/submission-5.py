class Solution:
    def findMin(self,nums):
        if nums[0] < nums[-1]:
            return nums[0]
        elif len(nums) == 1:
            return nums[0]
            
        l = 0
        r = len(nums) - 1
        result = nums[r]
        while (r - l) != 1:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid
            elif nums[mid] < nums[r]:
                if nums[mid] < result:
                    result = nums[mid]
                    r = mid
                else:
                    break
        return result
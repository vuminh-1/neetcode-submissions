class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = nums[0]
        for i in nums:
            if min > i:
                min = i
        return min
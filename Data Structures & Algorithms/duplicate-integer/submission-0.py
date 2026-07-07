class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                return True
        return False
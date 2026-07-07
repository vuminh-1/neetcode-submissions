class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        elif target < nums[0]:
            return -1
        elif target > nums[-1]:
            return -1
        else:
            l = 0
            r = len(nums) - 1
            while l != r:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    mid = (l + r) // 2
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] > target:
                        r = mid - 1
                    elif nums[mid] < target:
                        l = mid + 1

            return -1
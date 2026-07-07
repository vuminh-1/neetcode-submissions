class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[-1] == target:
                return 1
            else:
                return -1

        if nums[0] < nums[-1]:              
            print("TH1")
            if target < nums[0]:
                return -1
            elif target > nums[-1]:
                return -1

            l = 0
            r = len(nums) - 1
            while l != r:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r

                mid = (l+r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        elif nums[0] == nums[-1]:           
            print("TH2")
            if nums[0] != target:
                return -1
            else:
                return 0

        else:                               
            print("TH3")
            l = 0 
            r = len(nums) - 1
            while l != r:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r

                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < nums[r]:
                    if target > nums[mid] and target < nums[r]:
                        l = mid + 1
                    elif target > nums[mid] and target > nums[r]:
                        r = mid - 1
                    elif target < nums[mid]:
                        r = mid - 1
                    
                elif nums[mid] > nums[r]:
                    if target > nums[mid]:
                        l = mid + 1
                    elif target < nums[mid] and target < nums[r]:
                        l = mid + 1
                    elif target < nums[mid] and target > nums[r]:
                        r = mid - 1
                    
            return -1

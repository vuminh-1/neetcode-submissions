class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def flat(matrix):
            flatten = []
            for i in matrix:
                flatten.extend(i)
            return flatten
        
        def search(flatten,target):
            l = 0
            r = len(flatten) - 1
            if flatten[l] == target:
                return True
            elif flatten[r] == target:
                return True
            while l != r:
                if target < flatten[l]:
                    return False
                elif target > flatten[r]:
                    return False
                elif flatten[l] == target:
                    return True
                elif flatten[r] == target:
                    return True
                else:
                    mid = (l + r) // 2
                    if flatten[mid] == target:
                        return True
                    elif flatten[mid] < target:
                        l = mid + 1
                    elif flatten[mid] > target:
                        r = mid - 1

            return False
        flatten = flat(matrix)
        return search(flatten,target)

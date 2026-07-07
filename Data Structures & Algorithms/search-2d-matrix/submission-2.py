class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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
        for i in range(len(matrix)):
            if target < matrix[i][0]:
                return False
            elif target >= matrix[i][0] and target <= matrix[i][-1]:
                return search(matrix[i],target)
            elif target > matrix[i][-1]:
                continue
        
        return False


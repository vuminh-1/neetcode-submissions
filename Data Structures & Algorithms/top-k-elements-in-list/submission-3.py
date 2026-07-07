class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction = {}
        for i in nums:
            if i not in diction:
                diction[i] = 1
            else:
                diction[i] += 1
        
        diction = dict(sorted(diction.items(), key = lambda item: item[1], reverse = True))
        if k > len(diction):
            a = []
            for i in diction:
                a.append(int(i))
            return a
        else:
            a = []
            count = 0
            for i in diction:
                if count < k:
                    a.append(int(i))
                    count += 1
                else:
                    break 
            return a



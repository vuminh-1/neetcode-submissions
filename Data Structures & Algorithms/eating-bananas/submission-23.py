class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(piles,rate):
            l = len(piles)
            hours = 0
            for i in range(l):
                if rate >= piles[i]:
                    hours += 1
                elif piles[i] % rate == 0: 
                    hours += piles[i] // rate
                else:
                    hours += piles[i] // rate + 1
            return hours

        if h == len(piles):
            return max(piles)
        elif h == check(piles,min(piles)):
            return min(piles)


                
        l = 1
        r = max(piles)
        rate = 0
        result = 0
        while l <= r:
            rate = (l + r) // 2
            compared_hours = check(piles,rate)
            if compared_hours > h:
                l = rate + 1
            elif compared_hours <= h:
                result = rate
                r = rate - 1
            

        return result
        
        



            




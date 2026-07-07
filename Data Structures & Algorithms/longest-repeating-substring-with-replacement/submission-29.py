class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def show(s,k,character):
            l = 0
            r = 0
            count = 0
            result = 0
            while r < len(s):
                if s[r] != character and k > 0:
                    count += 1
                    k -= 1
                    r += 1
                elif s[r] != character and k == 0:
                    if s[l] == character:
                        while s[l] == character:
                            l += 1
                            count -= 1
                    elif s[l] != character:
                        pass
                    l += 1
                    r += 1
                elif s[r] == character:
                    count += 1
                    r += 1
                if result < count:
                    result = count
                else:
                    pass
            return result


        diction = {}
        for i in s:
            if i not in diction:
                diction[i] = 1
            else:
                diction[i] += 1
        
        max_count = 0
        for i in diction:
            temp = show(s,k,i)
            if max_count < temp:
                max_count = temp
            else:
                pass
        return max_count

        
        
        

        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        elif len(s) == 2:
            if s[0] != s[-1]:
                return 2
            else:
                return 1
        else:
            max_l = 1
            length = 0
            l = 0
            r = l + 1
            while r < len(s):
                if s[r] not in s[l:r]:
                    length = r - l + 1
                    max_l = max(max_l,length)
                    r += 1
                else:
                    length = r - l
                    max_l = max(max_l,length)
                    while s[r] in s[l:r]:
                        l += 1
                    r += 1
            
            return max_l
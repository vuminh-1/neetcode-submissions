class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            dict = {}
            dict1 = {}
            for i in range(len(s)):
                if s[i] not in dict:
                    dict[s[i]] = 1
                else:
                    dict[s[i]] += 1
                
                if t[i] not in dict1:
                    dict1[t[i]] = 1
                else:
                    dict1[t[i]] += 1
        
            if dict == dict1:
                return True
            else:
                return False

                
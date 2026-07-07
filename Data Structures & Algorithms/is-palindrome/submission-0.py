class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(x):
            if ord(x) in range(48,58):
                return True
            elif ord(x) in range(97,123):
                return True
            elif ord(x) in range(65,92):
                return True
            else:
                return False
        
        c = ''
        for i in s:
            if check(i):
                c += i.lower()
        
        for i in range(len(c)//2):
            if c[i] == c[len(c) - i - 1]:
                pass
            else:
                return False

        return True

        
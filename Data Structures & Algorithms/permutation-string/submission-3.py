class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def compare(characters,check):
            if len(check) != len(characters):
                return False
            else:
                for i,j in characters.items():
                    if check[i] != j:
                        return False
                    else:
                        pass
                
                return True

        if s1 in s2:
            return True
        else:
            pass
        characters = {}
        for i in s1:
            if i not in characters:
                characters[i] = 1
            else:
                characters[i] += 1
        
        l = 0 
        r = 1
        check = {}
        while r < len(s2):
            if s2[l] not in characters:
                check = {}
                l += 1
                r = l + 1
            else:
                if s2[l] not in check:
                    check[s2[l]] = 1
                

                if s2[r] in characters:
                    if s2[r] not in check:
                        check[s2[r]] = 1
                    else:
                        check[s2[r]] += 1

                    if r - l + 1 < len(s1):
                        if check[s2[r]] > characters[s2[r]]:
                            check = {}
                            l += 1
                            r = l + 1
                        else:
                            r += 1
                            pass
                    elif r - l + 1 == len(s1):
                        print(check)
                        if check[s2[r]] > characters[s2[r]]:
                            check = {}
                            l += 1
                            r = l + 1
                        else:
                            if compare(characters,check):
                                return True
                            else:
                                check = {}
                                l += 1
                                r = l + 1
                        
                elif s2[r] not in characters:
                    check = {}
                    l = r + 1
                    r += 2

        
        return False
                    






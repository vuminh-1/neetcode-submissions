class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        characters = {}

        def compare(dict1,dict2):
            for i,j in dict1.items():
                if dict2[i] < j:
                    return 'less'
                else:
                    pass
            return 'equal'

        for i in t:
            if i not in characters:
                characters[i] = 1
            else:
                characters[i] += 1
        

        l = 0
        r = l 
        check = {}
        min_len = 0
        result = ''
        while r < len(s) and l < len(s):
            if s[l] not in characters:
                l += 1
                r = l
            else:
                if s[r] in characters and s[r] not in check:
                    check[s[r]] = 1
                elif s[r] in characters and s[r] in check:
                    check[s[r]] += 1 
                else:
                    r += 1
                    continue
                
                if len(check) < len(characters):
                    r += 1
                    continue
                elif len(check) == len(characters):
                    print(s[l:r+1])
                    if compare(characters,check) == 'equal':
                        #gan gia tri max
                        if min_len == 0:
                            min_len = r - l + 1
                            result = s[l:r+1]
                        else:
                            if r - l + 1 < min_len:
                                min_len = r - l + 1
                                result = s[l:r+1]
                            else:
                                pass
                        
                        while s[l] in characters:
                            check[s[l]] -= 1
                            l += 1
                            if compare(characters,check) == 'equal':
                                #gan gia tri min
                                if min_len == 0:
                                    min_len = r - l + 1
                                    result = s[l:r+1]
                                else:
                                    if r - l + 1 < min_len:
                                        min_len = r - l + 1
                                        result = s[l:r+1]
                                    else:
                                        pass
                            print(s[l:r+1])
                            if l >= len(s):
                                break
                        if l >= len(s):
                            break
                        while s[l] not in characters:
                            l += 1
                            if compare(characters,check) == 'equal':
                                #gan gia tri min
                                if min_len == 0:
                                    min_len = r - l + 1
                                    result = s[l:r+1]
                                else:
                                    if r - l + 1 < min_len:
                                        min_len = r - l + 1
                                        result = s[l:r+1]
                                    else:
                                        pass
                            if l >= len(s):
                                break
                            
                           
                        r += 1
                    else:
                        r += 1


        if l < r:
            if compare(characters,check) == 'equal':
                if min_len == 0:
                    min_len = r - l + 1
                    result = s[l:r+1]
                else:
                    if r - l + 1 < min_len:
                        min_len = r - l + 1
                        result = s[l:r+1]
                    else:
                        pass


        return result

                
                
                    
                    
                





        
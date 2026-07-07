class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def check(s,s1):
            if len(s) != len(s1):
                return False
            else:
                dict1 = {}
                dict2 = {}
                for i in range(len(s)):
                    if s[i] not in dict1:
                        dict1[s[i]] = 1
                    else:
                        dict1[s[i]] += 1
                    
                    if s1[i] not in dict2:
                        dict2[s1[i]] = 1
                    else:
                        dict2[s1[i]] += 1
            if dict1 == dict2:
                return True
            else:
                return False
        
        #main 
        if len(strs) == 1:
            return [strs]
        elif len(strs) == 2:
            if check(strs[0],strs[1]):
                return [[strs[0],strs[1]]]
            else:
                return [[strs[0]],[strs[1]]]
        else:
            result = []
            mark = [0]*len(strs)
            for i in range(len(strs)-1):
                if mark[i] == 0:
                    result.append([strs[i]])
                    mark[i] = 1
                    for j in range(i+1,len(strs)):
                        if check(strs[i],strs[j]):
                            result[-1].append(strs[j])
                            mark[j] = 1
                        else:
                            pass
                else:
                    pass
            
            if mark[-1] == 0:
                result.append([strs[-1]])
            else:
                pass
            
            return result 









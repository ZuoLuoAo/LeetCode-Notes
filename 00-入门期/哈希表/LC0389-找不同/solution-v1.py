class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic_s = {}
        dic_t = {}

        for i in s:
            if i in dic_s:
                dic_s[i] += 1
            else:
                dic_s[i] = 0
        
        for i in t:
            if i in dic_t:
                dic_t[i] += 1
            else:
                dic_t[i] = 0
        
        list_s = list(dic_s.keys())
        list_t = list(dic_t.keys())
        list_s.sort()
        list_t.sort()

        if list_s != list_t:
            for i in dic_t.keys():
                if i not in dic_s:
                    return i

        else:
            for i in dic_t.keys():
                if dic_s[i] != dic_t[i]:
                    return i

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            dic_s = {}
            dic_t = {}

            for i, j in zip(s, t):
                if i not in dic_s:
                    dic_s[i] = 0
                else:
                    dic_s[i] += 1

                if j not in dic_t:
                    dic_t[j] = 0
                else:
                    dic_t[j] += 1
            
            if dic_s == dic_t:
                return True
            else:
                return False

        else:
            return False

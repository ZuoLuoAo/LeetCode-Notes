class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        num = 0
        ans = []
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i+1 : i+len(needle)] == needle[1 : len(needle)]:
                    num = i 
                    ans.append(num)
               
        print(ans)
        if not ans:
            return -1
        else:
            return ans[0]

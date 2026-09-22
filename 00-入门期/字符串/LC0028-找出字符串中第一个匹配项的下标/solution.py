class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # num 存命中的下标，ans 收集所有命中的位置
        num = 0
        ans = []
        
        # 逐个起点试：首字符对上，再比后面那一段
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                # 剩余部分用切片整体比较
                if haystack[i+1 : i+len(needle)] == needle[1 : len(needle)]:
                    num = i 
                    ans.append(num)
               
        # 一个都没命中就返回 -1，否则返回第一个命中位置
        if not ans:
            return -1
        else:
            return ans[0]

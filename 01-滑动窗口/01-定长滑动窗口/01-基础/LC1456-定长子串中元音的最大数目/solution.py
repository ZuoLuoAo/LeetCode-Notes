class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        nums = ['a', 'e', 'i', 'o', 'u']

        # 先把第一个窗口的元音数数出来
        ks = s[0:k]
        any = 0
        ans = 0

        for i in ks:
            if i in nums:
                any += 1
                ans = max(ans, any)
                if ans == k:
                    return ans

        # 窗口整体往右滑一格：左端出去一个，右端进来一个
        for i in range(len(s)-k):
            if s[i] in nums:
                any -= 1
        
            if s[i+k] in nums:
                any += 1
                ans = max(ans, any)
                if ans == k:
                    return ans

        return ans

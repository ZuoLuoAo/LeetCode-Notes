class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt = {}
        for ch in s:
            cnt[ch] = cnt.get(ch, 0) + 1
        for ch in t:
            cnt[ch] = cnt.get(ch, 0) - 1
            if cnt[ch] < 0:
                return ch

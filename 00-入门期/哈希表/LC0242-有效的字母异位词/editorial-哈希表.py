class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = {}
        for ch in s:
            table[ch] = table.get(ch, 0) + 1
        for ch in t:
            table[ch] = table.get(ch, 0) - 1
            if table[ch] < 0:
                return False
        return True

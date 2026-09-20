class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sums = sum(ord(i) for i in s)
        sumt = sum(ord(i) for i in t)

        return chr(sumt - sums)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 分别求 s 和 t 的 ASCII 码之和
        sums = sum(ord(i) for i in s)
        sumt = sum(ord(i) for i in t)

        # t 只比 s 多一个字符，差值就是那个字符的 ASCII 码
        return chr(sumt - sums)

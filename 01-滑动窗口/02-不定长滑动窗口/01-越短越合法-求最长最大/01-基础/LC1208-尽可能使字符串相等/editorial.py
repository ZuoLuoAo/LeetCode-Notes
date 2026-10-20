class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_length = 0
        left = 0
        cost = 0
        for right, x in enumerate(s):
            cost += abs(ord(s[right]) - ord(t[right]))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_length = max(max_length, right + 1 - left)

        return max_length

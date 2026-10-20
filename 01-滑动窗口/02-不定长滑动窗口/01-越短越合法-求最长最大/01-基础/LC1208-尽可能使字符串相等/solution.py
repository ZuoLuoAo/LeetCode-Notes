class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        # 力扣要求的签名留在外层，滑窗逻辑收进内层函数
        def solve(s, t, maxCost):
            ans = 0
            left = 0
            cost = 0

            # 右端逐格进入，累加当前位置的修改代价
            for i, j in enumerate(s):
                cost += abs(ord(s[i]) - ord(t[i]))

                # 代价超预算时，从左端逐个移出，直到窗口重新合法
                while cost > maxCost:
                    cost -= abs(ord(s[left]) - ord(t[left]))
                    left += 1

                # 当前窗口整体可改，更新最大长度
                ans = max(ans, i - left + 1)

            return ans

        return solve(s, t, maxCost)

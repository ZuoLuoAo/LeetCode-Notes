class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        # 力扣要的签名留在外层，滑窗逻辑收进内层函数
        def solve(cardPoints, k):
            n = len(cardPoints) - k

            # 反着算：拿走的 k 张 = 总和 - 剩下的连续 n 张；k 等于数组长度时窗口是空的
            if n == 0:
                return sum(cardPoints)

            ans = sum(cardPoints)
            s = 0

            # 右端点逐格推进，把长度 n 的窗口一格一格撑起来
            for i, j in enumerate(cardPoints):
                s += j

                # 窗口还没攒够 n 个元素
                if i-n+1 < 0:
                    continue

                # 窗口满了：先比一次和，再让左端的元素出去
                ans = min(s, ans)
                s -= cardPoints[i-n+1]

            return sum(cardPoints) - ans

        return solve(cardPoints, k)

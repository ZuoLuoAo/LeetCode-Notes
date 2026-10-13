class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        # 力扣要的签名留在外层，滑窗逻辑收进内层函数
        def solve(blocks, k):
            ans = ans_max = 0

            # 右端点逐格推进：先进窗口，凑够 k 个再更新答案，最后左端出去
            for i, j in enumerate(blocks):
                if j == 'B':
                    ans += 1

                if i-k+1 < 0:
                    continue

                # 窗口已经全是黑块，一次都不用涂
                if ans == k:
                    return 0

                ans_max = max(ans, ans_max)

                if blocks[i-k+1] == 'B':
                    ans -= 1

            return k-ans_max

        return solve(blocks, k)

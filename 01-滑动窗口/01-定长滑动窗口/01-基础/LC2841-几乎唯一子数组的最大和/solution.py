class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:

        # 力扣要的签名留在外层，滑窗逻辑收进内层函数
        def solve(nums, m, k):
            lyst = []
            ans = 0

            # 右端点逐格推进，新元素进窗口
            for i, j in enumerate(nums):
                lyst.append(j)

                # 窗口还没攒够 k 个元素
                if len(lyst) < k:
                    continue

                # 窗口里互不相同的元素不足 m 个，这个窗口不合法
                if len(set(lyst)) < m:
                    lyst = lyst[1:]
                    continue

                # 合法窗口：先比一次和，再让左端的元素出去
                ans = max(sum(lyst), ans)

                lyst = lyst[1:]

            return ans

        return solve(nums, m, k)

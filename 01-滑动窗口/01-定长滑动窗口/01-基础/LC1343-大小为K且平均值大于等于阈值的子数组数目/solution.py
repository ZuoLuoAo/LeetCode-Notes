class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:

        # 力扣要的签名留在外层，滑窗逻辑收进内层函数
        def solve(arr, k, threshold):
            num, ans = 0, 0

            # 右端点逐格推进：先进窗口，凑够 k 个再判平均值，最后左端出去
            for i in range(len(arr)):
                num += arr[i]

                if i-k+1 < 0:
                    continue

                average = num/k
                if average >= threshold:
                    ans += 1

                num -= arr[i-k+1]

            return ans

        return solve(arr, k, threshold)

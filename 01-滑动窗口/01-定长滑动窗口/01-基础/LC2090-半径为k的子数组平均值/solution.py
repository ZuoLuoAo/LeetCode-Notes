class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        def solve(nums, k):
            ans = sum(nums[:k*2])
            ans_lyst = []

            for i, j in enumerate(nums):

                if i-k < 0 or i+k >= len(nums):
                    ans_lyst.append(-1)
                    continue

                ans += nums[i+k]
                ans_lyst.append(ans//(k*2+1))
                ans -= nums[i-k]

            return ans_lyst

        return solve(nums, k)

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()  # 排序后，能留下的元素一定是连续的一段

        max_save = left = 0  # 最多能保留的元素个数；窗口左端点
        for i, mx in enumerate(nums):  # 枚举窗口右端点，mx 是当前窗口最大值
            while nums[left] * k < mx:  # 最小值撑不起最大值，缩小窗口
                left += 1
            max_save = max(max_save, i - left + 1)  # 当前窗口整段都能留下

        return len(nums) - max_save  # 窗口以外的元素都得删掉

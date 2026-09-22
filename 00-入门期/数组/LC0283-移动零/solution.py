class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 先数出一共有几个 0
        num = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                num += 1

        # 末尾 num 个位置最后一定全是 0，所以只需要管前面的部分
        i = 0
        while i < len(nums)-num:
            if nums[i] == 0:

                # 把这个 0 一路往右冒泡，直到沉到那段末尾
                for j in range(i, len(nums)-1):
                    nums[j], nums[j+1] = nums[j+1], nums[j]

            # 冒泡换上来的是非 0，这一位才算站住了
            if nums[i] != 0:
                i += 1

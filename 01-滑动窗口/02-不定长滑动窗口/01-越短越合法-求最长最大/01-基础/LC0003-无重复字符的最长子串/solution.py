class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # 力扣要的签名留在外层，滑窗逻辑收进内层函数
        def solve(s):
            length = 0
            dic = {}
            left = 0

            # 右端点逐格推进，新字符进窗口
            for i, j in enumerate(s):

                # 窗口里还没出现过这个字符：记一笔，窗口变长
                if j not in dic:
                    dic[j] = 1
                    length = max(length, len(dic))

                # 出现过：从左边一个个删，直到把它的上一次出现也删掉
                else:
                    dic[j] += 1

                    while True:
                        dic[s[left]] -= 1

                        # 计数减到 0 就删键，保证 len(dic) 就是窗口长度
                        if dic[s[left]] == 0:
                            del dic[s[left]]

                        # 删到重复字符自己，窗口重新无重复
                        if s[left] == j:
                            left += 1
                            break

                        left += 1

            return length

        return solve(s)

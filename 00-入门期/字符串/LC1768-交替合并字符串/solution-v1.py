class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 两个串差多少
        long = len(word1) - len(word2)

        # 挑出长的那个串
        maxstr = word1
        if long < 0:
            maxstr = word2

        # 开一个够长的列表，交替的位置先占住
        result = [0]*(len(maxstr) - abs(long))*2


        # word1 填偶数位
        for i, j in zip(word1, range(0, (len(maxstr)-abs(long))*2-1, 2)):
            result[j] = i

        # word2 填奇数位
        for i, j in zip(word2, range(1, (len(maxstr)-abs(long))*2, 2)):
            result[j] = i

        # 长串多出来的尾巴直接接到末尾
        for k in maxstr[len(maxstr)-abs(long):len(maxstr)]:
            result.append(k) 

        # 拼成一个字符串返回
        resultstr = ''.join(result)

        return resultstr

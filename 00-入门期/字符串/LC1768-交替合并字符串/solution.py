class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # i 是当前取到第几位，ans 用来存结果
        i = 0
        ans = []

        # 只要还有串没取完就继续
        while i <= len(word1) or i <= len(word2):
            # 这个位置 word1 还有字符就取出来
            if i < len(word1):
                ans.append(word1[i])
            
            # word2 同理
            if i < len(word2):
                ans.append(word2[i])
            
            i += 1
        
        # 拼成字符串返回
        return ''.join(ans)

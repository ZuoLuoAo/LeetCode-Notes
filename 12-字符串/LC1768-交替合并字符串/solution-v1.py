class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        long = len(word1) - len(word2)

        maxstr = word1
        if long < 0:
            maxstr = word2

        result = [0]*(len(maxstr) - abs(long))*2


        for i, j in zip(word1, range(0, (len(maxstr)-abs(long))*2-1, 2)):
            result[j] = i

        for i, j in zip(word2, range(1, (len(maxstr)-abs(long))*2, 2)):
            result[j] = i

        for k in maxstr[len(maxstr)-abs(long):len(maxstr)]:
            result.append(k) 

        resultstr = ''.join(result)

        return resultstr

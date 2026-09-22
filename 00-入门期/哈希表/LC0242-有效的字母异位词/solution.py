class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            # 建两张空表，分别统计 s 和 t
            dic_s = {}
            dic_t = {}

            # 两串等长，可以并排着一位一位扫
            for i, j in zip(s, t):
                # s 的这一位记一次数
                if i not in dic_s:
                    dic_s[i] = 0
                else:
                    dic_s[i] += 1

                # t 的这一位记一次数
                if j not in dic_t:
                    dic_t[j] = 0
                else:
                    dic_t[j] += 1

            # 两张表完全一样，说明 t 就是 s 重排出来的
            if dic_s == dic_t:
                return True
            else:
                return False

        # 长度都不一样，直接判不是
        else:
            return False

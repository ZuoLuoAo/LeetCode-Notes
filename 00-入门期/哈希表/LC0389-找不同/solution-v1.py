class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 建两张空表，分别统计 s 和 t
        dic_s = {}
        dic_t = {}

        # 数 s 里每个字符出现几次
        for i in s:
            if i in dic_s:
                dic_s[i] += 1
            else:
                dic_s[i] = 0
        
        # 数 t 里每个字符出现几次
        for i in t:
            if i in dic_t:
                dic_t[i] += 1
            else:
                dic_t[i] = 0
        
        # 把两张表的键排好序，方便直接比较
        list_s = list(dic_s.keys())
        list_t = list(dic_t.keys())
        list_s.sort()
        list_t.sort()

        # 键不一样：t 里那个 s 没有的键就是答案
        if list_s != list_t:
            for i in dic_t.keys():
                if i not in dic_s:
                    return i

        # 键一样：说明新增的字符 s 里本来就有，只能比计数
        else:
            for i in dic_t.keys():
                if dic_s[i] != dic_t[i]:
                    return i

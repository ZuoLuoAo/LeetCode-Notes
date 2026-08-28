---
id: LC1768
title: 交替合并字符串
aliases: [Merge Strings Alternately]
difficulty: 简单
tags: [字符串, 双指针]
status: 初次
first_date: 2026-08-29
last_review: 2026-08-29
link: https://leetcode.cn/problems/merge-strings-alternately/
---

# LC1768 · 交替合并字符串（Merge Strings Alternately）

> 说明：LeetHub 自动同步时因中文站解析 bug 将题号记为 1894（标题显示 undefined）；本题正确题号为 **1768**，本笔记以 1768 为准。

## 题目摘要

给定两个字符串 `word1`、`word2`，从 `word1` 开始交替取字符合并成一个字符串；较长字符串剩余的部分直接追加到末尾。约束：长度 1~100，仅含小写字母，O(m+n) 时间即可。

## 我的代码（第一次 AC）

来源：LeetCode-Raw 原始提交，原样内嵌（仅 Python；C++ 本次未提交）。

```python
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
```

## 我的代码总结

- 核心思路：先判断哪个串更长（`maxstr`），公共长度部分交替填入 `result` 的偶数/奇数位，再把长串多出的尾部 `append` 进去。
- 冗长点：
  1. 长度反复计算：`len(maxstr) - abs(long)` 多处重复，本质就是"较短串的长度"，一个 `min(len(word1), len(word2))` 就能说清楚。
  2. `result = [0]*...` 用整数 `0` 占位后填字符，类型混用；用 `['']*n` 更直观。
  3. 用 `zip(word1, range(起点, 终点, 步长))` 手动造索引，起止和步长都要心算，容易出错、可读性差。
  4. 尾部剩余字符先切片再循环 `append`，其实可以直接 `result.extend(...)`。
  5. 命名偏模糊：`maxstr`、`long`、`resultstr` 含义不直观。
- 值得肯定：最终用 `''.join(result)` 拼接而不是逐字符 `+`，思路是对的。

## 题解思路

官方解法 · 方法一：直接模拟 —— 按索引同时遍历两个字符串，`i < len(word1)` 就取 `word1[i]`，`i < len(word2)` 就取 `word2[i]`；不用预先区分长短，短的取完后长的自然继续输出。Python 用 `zip_longest(word1, word2, fillvalue='')` 可以一行完成。

## 官方题解代码

来源：力扣官方题解 · 方法一 直接模拟（经 [doocs/leetcode 镜像](https://github.com/doocs/leetcode/blob/main/solution/1700-1799/1768.Merge%20Strings%20Alternately/README.md) 整理；Python 省略的 `import` 语句已补全）。

### Python

```python
from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
```

### C++

```cpp
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        string ans;
        for (int i = 0; i < m || i < n; ++i) {
            if (i < m) ans += word1[i];
            if (i < n) ans += word2[i];
        }
        return ans;
    }
};
```

## 代码对比

| 维度 | 我的代码 | 官方题解 |
| --- | --- | --- |
| 思路 | 先区分长短，公共部分交替填位，尾部追加 | 直接按索引同时取两个串，不区分长短 |
| 结构 | 3 个循环 + 长度预计算 | 1 个循环（Python 一行） |
| 命名 | maxstr / long / resultstr，语义模糊 | 无额外变量，m、n 直观 |
| 复杂度 | O(m+n) 时间 / O(m+n) 空间 | O(m+n) 时间 / O(1) 空间（不计答案） |
| 可读性 | range 起止步长需心算，易错 | 直译题意，几乎不会写错 |

学到的一点：交替合并的本质是"按索引同时取两个串"，不需要预先区分长短——短的取完自然结束，多出的部分由长串尾部自然补齐。

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 我的解法 | O(m+n) | O(m+n) |
| 官方解法 | O(m+n) | O(1)（不计答案） |

## 易错点 / 复盘

- LeetHub 中文站解析 bug 导致原始仓库题号显示 1894、标题 undefined；正确题号为 1768，以本笔记为准。
- 不需要预先算长短：交替合并直接按索引取即可。
- Python 拼接字符串用 `''.join(列表)`，避免循环里逐字符 `+`。
- 关联问题：暂无（后续遇到双指针/模拟类题目时在此补充）。

## 复习记录

- 2026-08-29：首次 AC；思路为先区分长短再交替填入，代码偏冗长，已对照官方模拟解法。

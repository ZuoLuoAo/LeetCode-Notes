---
id: LC0028
title: 找出字符串中第一个匹配项的下标
aliases: [Find the Index of the First Occurrence in a String, 实现 strStr]
difficulty: 简单
tags: [字符串, 双指针]
status: 初次
first_date: 2026-08-29
last_review: 2026-08-29
link: https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
leet_dir: 0028-find-the-index-of-the-first-occurrence-in-a-string
last_leet_commit: 56e4c0c
---

# LC0028 · 找出字符串中第一个匹配项的下标（Find the Index of the First Occurrence in a String）

## 题目摘要

在 `haystack` 中找出 `needle` 第一次出现的下标，不存在返回 `-1`。约束：两个字符串长度均 ≥ 1，仅含小写字母。

## 我的代码（第一次 AC）

来源：LeetCode-Raw 原始提交（`0028-find-the-index-of-the-first-occurrence-in-a-string.py`，commit `56e4c0c`），原样内嵌，一字不改。

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        num = 0
        ans = []
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i+1 : i+len(needle)] == needle[1 : len(needle)]:
                    num = i 
                    ans.append(num)
               
        print(ans)
        if not ans:
            return -1
        else:
            return ans[0]
```

## 我的代码总结

- 核心思路：遍历 `haystack`，找到与 `needle` 首字符相同的位置 `i` 后，用切片比较剩余部分是否等于 `needle` 的后半段；把所有命中下标收进 `ans`，最后取第一个。
- 问题点：
  1. 直接访问 `needle[0]`，依赖题目"两个字符串均非空"的约束；若允许空串会 `IndexError`。
  2. 用 `ans` 列表收集所有命中位置再取 `ans[0]`，其实第一次命中就能直接 `return i`，列表多余。
  3. 残留调试代码 `print(ans)`，提交时应删掉。
  4. 切片比较写成 `haystack[i+1 : i+len(needle)] == needle[1 : len(needle)]` 绕了一圈；直接 `haystack[i : i+len(needle)] == needle` 更直白。
- 值得肯定：用切片整体比较代替手写内层循环，思路简单直接。

## 题解思路

官方解法方法一为暴力匹配（朴素匹配）：枚举每个可能起点 `i`（0 到 `n-m`），逐位比较 `haystack[i+j]` 与 `needle[j]`，内层循环全部相等时返回 `i`。方法二为 KMP：构造 `next` 数组，让主串指针不回退，把最坏复杂度从 O(n·m) 降到 O(n+m)。本题数据范围小，方法一足够；KMP 作为进阶选学。

## 官方题解代码

来源：力扣官方题解。题解页：https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/solution/

### Python（方法一：暴力匹配）

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1
```

### Python（方法二：KMP，进阶选学）

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        nxt = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and needle[i] != needle[j]:
                j = nxt[j - 1]
            if needle[i] == needle[j]:
                j += 1
            nxt[i] = j
        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = nxt[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1
```

> 注：KMP 按官方思路整理的 Python3 实现，细节以题解页为准。

## 代码对比

| 维度 | 我的代码 | 官方题解 |
| --- | --- | --- |
| 思路 | 命中首字符后用切片比较剩余 | 枚举起点逐位比较，`for-else` 收尾 |
| 结构 | 外层循环 + 切片 + `ans` 列表收集 | 双层循环，命中即返回 |
| 边界 | 依赖 `needle` 非空，未处理空串 | 空 `needle` 也正确返回 0 |
| 可读性 | 残留 `print`、列表多此一举 | 无多余变量，直译题意 |
| 复杂度 | O(n·m) 时间 / O(n) 空间 | O(n·m) 时间 / O(1) 空间 |

学到的一点：暴力匹配不需要"收集所有答案"，第一次命中就是答案；Python 的 `for-else` 可以在内层循环全部匹配成功时直接走 `else` 分支返回。

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 我的解法 | O(n·m) | O(n)（`ans` 列表） |
| 官方解法（暴力） | O(n·m) | O(1) |
| KMP（进阶） | O(n+m) | O(m) |

## 易错点 / 复盘

- 直接访问 `needle[0]` 前要确认题目是否允许空串；稳妥写法先判空。
- 第一次命中即可返回，不要收集所有位置。
- 切片比较前后两段要对应好：`haystack[i:i+m] == needle` 最直观。
- 关联问题：[[Python-列表#判断列表是否为空|判断列表是否为空]]（`if not ans` 判空）。

## 复习记录

- 2026-08-29：首次 AC；用切片 + `ans` 列表实现，思路对但结构冗余，已对照官方暴力匹配 + `for-else`。

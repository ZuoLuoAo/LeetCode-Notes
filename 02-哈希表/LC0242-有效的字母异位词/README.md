---
id: LC0242
title: 有效的字母异位词
aliases: [Valid Anagram]
difficulty: 简单
tags: [哈希表, 字符串, 排序]
status: 初次
first_date: 2026-08-29
last_review: 2026-08-29
link: https://leetcode.cn/problems/valid-anagram/
leet_dir: 0242-valid-anagram
last_leet_commit: 02ded29
---

# LC0242 · 有效的字母异位词（Valid Anagram）

## 题目摘要

判断 `t` 是否由 `s` 重排而成：两串长度相同且每个字符出现次数相同。`s`、`t` 仅含小写字母。

## 我的代码（第一次 AC）

来源：LeetCode-Raw 原始提交（`0242-valid-anagram.py`，commit `02ded29`），原样内嵌，一字不改。

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            dic_s = {}
            dic_t = {}

            for i, j in zip(s, t):
                if i not in dic_s:
                    dic_s[i] = 0
                else:
                    dic_s[i] += 1

                if j not in dic_t:
                    dic_t[j] = 0
                else:
                    dic_t[j] += 1
            
            if dic_s == dic_t:
                return True
            else:
                return False

        else:
            return False
```

## 我的代码总结

- 核心思路：先比长度；再分别统计 `s`、`t` 每个字符出现次数到两个字典；最后 `dic_s == dic_t` 判断是否相等。
- 问题点：
  1. 统计用 `if i not in dic_s: dic_s[i] = 0 else: dic_s[i] += 1`：首次出现记 0、再次出现才 +1，计数习惯与直觉相反（首次应记 1）。两串都这样写结果仍正确，但容易绕晕；`dic[i] = dic.get(i, 0) + 1` 一步完成更清晰。
  2. `len(s) == len(t)` 用 if/else 包住整段，可以提前 `return False`，减少嵌套。
  3. `if dic_s == dic_t: return True else: return False` 可以简化为 `return dic_s == dic_t`。
- 值得肯定：想到了"长度不同直接 False + 字典计数 + 字典比较"，思路方向完全正确。

## 题解思路

官方解法方法一为排序：`sorted(s) == sorted(t)`，重排后相等即异位词，一行完成，复杂度 O(n log n)。方法二为哈希表：先比长度，再统计 `s` 的字符计数，遍历 `t` 时逐个减 1，出现负数即返回 False，复杂度 O(n)。

## 官方题解代码

来源：力扣官方题解。题解页：https://leetcode.cn/problems/valid-anagram/solution/

### Python（方法一：排序）

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

### Python（方法二：哈希表）

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = {}
        for ch in s:
            table[ch] = table.get(ch, 0) + 1
        for ch in t:
            table[ch] = table.get(ch, 0) - 1
            if table[ch] < 0:
                return False
        return True
```

## 代码对比

| 维度 | 我的代码 | 官方题解 |
| --- | --- | --- |
| 思路 | 双字典分别计数后比较 | 一个字典：s 加、t 减，出现负数即失败 |
| 结构 | 长度判断包住整段 + 双字典 | 先比长度提前返回，单字典 |
| 计数写法 | `in` 判断 + 分支赋值（首次记 0） | `dict.get(key, 0) + 1` 一步完成 |
| 返回 | if/else 显式 `return True/False` | 直接返回比较/判断结果 |
| 复杂度 | O(n) / O(1)（字符集有限） | O(n) / O(1) |

学到的一点：哈希表计数可以"一个表双向用"——一个串加、另一个串减，最后天然抵消；`dict.get` 让计数从 3 行缩成 1 行。

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 我的解法 | O(n) | O(1)（字符集有限） |
| 官方（排序） | O(n log n) | O(1) |
| 官方（哈希表） | O(n) | O(1) |

## 易错点 / 复盘

- 先比长度：长度不同直接 False，避免后续统计白做。
- 计数别用"首次记 0、再出现 +1"的写法，容易自坑；`dict.get(key, 0) + 1` 更直观。
- 字典比较 `==` 只关心键值、顺序无关，适合"重排是否相同"这类判断。
- 关联问题：[[Python-字典#dict.get 默认值|dict.get 默认值]]、[[Python-字典#判断键是否存在|判断键是否存在]]、[[Python-字典#字典比较相等|字典比较相等]]、[[Python-列表#列表排序|列表排序]]（`sorted` 一行比较）。

## 复习记录

- 2026-08-29：首次 AC；双字典计数比较方向正确，对照官方学会 `dict.get` 一步计数与"一表双向增减"。

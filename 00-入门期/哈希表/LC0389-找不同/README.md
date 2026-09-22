---
id: LC0389
title: 找不同
aliases: [Find the Difference]
difficulty: 简单
tags: [哈希表, 位运算, 排序]
status: 复习中
first_date: 2026-08-29
last_review: 2026-08-30
link: https://leetcode.cn/problems/find-the-difference/
leet_dir: 0389-find-the-difference
last_leet_commit: 74a9250
---

# LC0389 · 找不同（Find the Difference）

## 题目摘要

`t` 由 `s` 随机重排后额外插入一个字符（位置不定），找出这个被添加的字符。

## 我的代码（第一次 AC）

来源：LeetCode-Raw 原始提交（commit `a60b5fd`），代码见 `solution-v1.py`，与力扣 AC 提交一字不差。

```dataviewjs
dv.paragraph("```python\n" + await dv.io.load("00-入门期/哈希表/LC0389-找不同/solution-v1.py") + "\n```")
```

## 我的代码（第二次 AC）

来源：LeetCode-Raw 原始提交（commit `74a9250`），代码见 `solution.py`，与力扣 AC 提交一字不差。

```dataviewjs
dv.paragraph("```python\n" + await dv.io.load("00-入门期/哈希表/LC0389-找不同/solution.py") + "\n```")
```

## 我的代码总结

- 核心思路：分别统计 `s`、`t` 的字符计数到两个字典；若键集合不同，返回 `t` 中独有的键；否则找到计数不同的那个键。
- 问题点：
  1. 计数同样是"首次记 0、再出现 +1"的写法，虽然能 AC，但反直觉、容易忘。
  2. 用 `keys()` + `sort()` 比较键集合绕了一圈：`t` 中"不在 `dic_s` 里的键"就是答案，无需排序；直接 `if i not in dic_s` 判断即可。
  3. 分支里遍历 `dic_t.keys()` 找计数不同的键，逻辑没问题但代码偏长；官方"一表双向增减"更短。
  4. 双字典方案整体 O(n) 但代码量大；求和 / 异或是一行级实现，更优雅。
- 值得肯定：想到了比较键集合 + 计数，覆盖了"新增字符已存在/不存在"两种情况，思路完整。
- 第二次 AC（2026-08-30）：直接采用 ASCII 求和差值（`sum(ord(...))` 相减），与官方方法二一致，6 行完成——"多一个字符"的求和套路已掌握。

## 题解思路

官方解法有三种：方法一计数——统计 `s` 中字符计数，遍历 `t` 逐个减 1，出现负数即答案；方法二求和——`sum(ord(t)) - sum(ord(s))` 的 ASCII 差值就是新增字符；方法三位运算——把 `s + t` 所有字符的 ASCII 值异或起来，出现偶数次的成对抵消，剩下的就是答案。本题"只多一个字符"，求和 / 异或天然适合。

## 官方题解代码

来源：力扣官方题解。题解页：https://leetcode.cn/problems/find-the-difference/solution/

### Python（方法一：计数）

```dataviewjs
dv.paragraph("```python\n" + await dv.io.load("00-入门期/哈希表/LC0389-找不同/editorial-计数.py") + "\n```")
```

### Python（方法二：求和）

```dataviewjs
dv.paragraph("```python\n" + await dv.io.load("00-入门期/哈希表/LC0389-找不同/editorial-求和.py") + "\n```")
```

### Python（方法三：位运算）

```dataviewjs
dv.paragraph("```python\n" + await dv.io.load("00-入门期/哈希表/LC0389-找不同/editorial-位运算.py") + "\n```")
```

## 代码对比

| 维度 | 我的代码 | 官方题解 |
| --- | --- | --- |
| 思路 | 双字典 + 键集合排序比较 | 一表双向增减 / ASCII 求和 / 异或 |
| 结构 | 两个统计循环 + 两个分支 | 计数版一个字典；求和版一行 |
| 计数写法 | `in` 判断 + 分支（首次记 0） | `dict.get(key, 0) + 1` |
| 代码量 | 33 行 | 计数版 11 行、求和版 1 行 |
| 复杂度 | O(n) / O(1) | O(n) / O(1) |

学到的一点："多出来的那一个"类问题，优先想三种武器：计数抵消、求和差值、异或抵消；本题求和与异或都是 O(n) 且常数极小。

> 2026-08-30 第二次 AC 已改写为 ASCII 求和差值（即官方方法二），代码从 33 行降至 6 行；上表对比仍以第一次 AC 为基准。

## 复杂度分析

| 解法 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 我的解法 | O(n) | O(1)（字符集有限） |
| 官方（计数） | O(n) | O(1) |
| 官方（求和/异或） | O(n) | O(1) |

## 易错点 / 复盘

- 新增字符可能已在 `s` 中出现（如 `s="a"`、`t="aa"`），只看键集合会漏，必须比对计数。
- "首次记 0"的计数写法能过但反直觉，统一用 `dict.get(key, 0) + 1`。
- 求和 / 异或方案依赖"只多一个字符"这一前提，题目变了要重新评估。
- 关联问题：[[Python-字典#dict.get 默认值|dict.get 默认值]]、[[Python-字典#提取所有键|提取所有键]]、[[Python-列表#列表排序|列表排序]]（排序键列表比较）。

## 复习记录

- 2026-08-29：首次 AC；双字典思路完整但冗长，已对照官方学习计数抵消、ASCII 求和、异或三种写法。
- 2026-08-30：重刷；改用 ASCII 求和差值，思路已贴近官方方法二，代码从 33 行降到 6 行。

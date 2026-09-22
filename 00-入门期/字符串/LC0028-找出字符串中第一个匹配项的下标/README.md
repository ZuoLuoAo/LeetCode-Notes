---
id: LC0028
title: 找出字符串中第一个匹配项的下标
tags: [字符串, 双指针]
link: https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
---

# LC0028 · 找出字符串中第一个匹配项的下标

在 `haystack` 里找 `needle` 第一次出现的下标，找不到返回 -1。两个串长度都 ≥ 1，只含小写字母。

## 我的代码

### 第一次 AC（2026-08-29）

```dataviewjs
dv.paragraph("```python\n" + await dv.io.load("00-入门期/字符串/LC0028-找出字符串中第一个匹配项的下标/solution.py") + "\n```")
```

## 官方题解

### 方法一：暴力匹配

```dataviewjs
dv.paragraph("```python\n" + await dv.io.load("00-入门期/字符串/LC0028-找出字符串中第一个匹配项的下标/editorial-暴力匹配.py") + "\n```")
```

### 方法二：KMP（进阶选学）

```dataviewjs
dv.paragraph("```python\n" + await dv.io.load("00-入门期/字符串/LC0028-找出字符串中第一个匹配项的下标/editorial-kmp.py") + "\n```")
```

## 对比

思路差别：我逐个起点试，首字符对上就用切片把后面一整段拿来比。官方暴力匹配是双层循环逐位比，内层全部相等时用 `for-else` 返回起点。

写法差别：我 16 行，官方暴力版 10 行。多出来的是 `ans` 列表和结尾的判空——这题第一次命中就是答案，不需要先把所有命中位置收集起来再取第一个。另外我取 `needle[0]` 前没考虑空串，官方暴力版靠 `range(n-m+1)` 天然处理掉了。KMP 那版 22 行，是进阶解法，本题的数据范围用不上。

复杂度：我的和官方暴力都是 O(n·m) 时间；我额外开了 `ans` 列表，官方是 O(1)。KMP 是 O(n+m) 时间、O(m) 空间。

## 复盘

- **核心思路**：找第一个匹配位置，第一次命中就能返回，不要先收集再挑。
- **踩的坑**：① 残留了一行 `print(ans)` 调试输出；② 切片写成 `haystack[i+1 : i+len(needle)] == needle[1 : len(needle)]`，前后两段要对应好才不出错，`haystack[i : i+m] == needle` 更直白；③ 直接取 `needle[0]`，题目虽然保证非空，换成允许空串的题就会 IndexError。
- **学到的**：Python 的 `for-else`——内层循环没被 `break` 打断时走 `else` 分支，正好用来表达"整段都匹配上了"。
- **关联问题**：[[Python-列表#判断列表是否为空]]

## 复习记录

| 日期 | 次数 | 结果 |
| --- | --- | --- |
| 2026-08-29 | 1 | 首次 AC |

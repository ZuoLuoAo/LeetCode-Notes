---
id: LC0389
title: 找不同
tags: [哈希表, 位运算, 排序]
link: https://leetcode.cn/problems/find-the-difference/
---

# LC0389 · 找不同

`t` 是 `s` 随机重排后又多插了一个字符，找出这个多出来的字符。

## 我的代码

### 第一次 AC（2026-08-29）

```dataviewjs
dv.paragraph("```python\n" + await dv.io.load("00-入门期/哈希表/LC0389-找不同/solution-v1.py") + "\n```")
```

### 第二次 AC（2026-08-30）

```dataviewjs
dv.paragraph("```python\n" + await dv.io.load("00-入门期/哈希表/LC0389-找不同/solution.py") + "\n```")
```

## 官方题解

### 方法一：计数

```dataviewjs
dv.paragraph("```python\n" + await dv.io.load("00-入门期/哈希表/LC0389-找不同/editorial-计数.py") + "\n```")
```

### 方法二：求和

```dataviewjs
dv.paragraph("```python\n" + await dv.io.load("00-入门期/哈希表/LC0389-找不同/editorial-求和.py") + "\n```")
```

### 方法三：位运算

```dataviewjs
dv.paragraph("```python\n" + await dv.io.load("00-入门期/哈希表/LC0389-找不同/editorial-位运算.py") + "\n```")
```

## 对比

思路差别：我用两张表分别统计 `s` 和 `t`，再比键集合、需要时再比计数。官方方法一只用一个表，`s` 加、`t` 减，减出负数就是答案；方法二方法三更短，ASCII 求和差值和异或抵消都是一行级。

写法差别：第一次 AC 31 行，官方计数版 9 行、求和版 3 行。多出来的部分全花在"先比键集合、再决定怎么找"这个分岔上，而这题根本不需要分岔。第二次 AC 换成求和后降到 6 行，和官方方法二同一个思路。

复杂度：都是 O(n) 时间、O(1) 空间。

## 复盘

- **核心思路**：找"多出来的那一个"，先想三件武器——计数抵消、ASCII 求和、异或抵消。
- **踩的坑**：以为"两张表的键不一样"就能定位答案，忽略了新增的字符 `s` 里本来就可能出现（`s="a"`、`t="aa"`），必须回头比计数——代码里那个 `if list_s != list_t` 分岔就是这么来的，绕了一圈。
- **学到的**：求和和异或这两条捷径都依赖"只多一个字符"这个前提，题目一变（比如多了两个）就失效。
- **关联问题**：[[Python-字典#dict.get 默认值]]、[[Python-字典#提取所有键]]、[[Python-列表#列表排序]]

## 复习记录

| 日期 | 次数 | 结果 |
| --- | --- | --- |
| 2026-08-29 | 1 | 首次 AC |
| 2026-08-30 | 2 | 重刷：改用 ASCII 求和差值，31 行降到 6 行 |

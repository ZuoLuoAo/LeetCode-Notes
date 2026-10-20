---
id: LC1208
title: 尽可能使字符串相等
tags: [滑动窗口]
link: https://leetcode.cn/problems/get-equal-substrings-within-budget/
---

# LC1208 · 尽可能使字符串相等

给两个长度相同的字符串 `s` 和 `t`，把 `s` 的某个连续子串逐位改成 `t` 的对应字符，第 `i` 位的修改代价是 `|s[i] - t[i]|`。总代价不超过 `maxCost` 时，返回能改成相等的子串最大长度。1 ≤ s.length ≤ 10⁵，t.length = s.length，0 ≤ maxCost ≤ 10⁶，两个字符串只含小写英文字母。

## 我的代码

### 第一次 AC（2026-10-20）

```dataviewjs
dv.paragraph("```python\n" + await dv.io.load("01-滑动窗口/02-不定长滑动窗口/01-越短越合法-求最长最大/01-基础/LC1208-尽可能使字符串相等/solution.py") + "\n```")
```

## 官方题解

来源：[力扣题解](https://leetcode.cn/problems/get-equal-substrings-within-budget/solutions/3702572/ling-shen-bu-ding-chang-hua-chuang-fang-mi0tt/)（作者：w）。

```dataviewjs
dv.paragraph("```python\n" + await dv.io.load("01-滑动窗口/02-不定长滑动窗口/01-越短越合法-求最长最大/01-基础/LC1208-尽可能使字符串相等/editorial.py") + "\n```")
```

## 对比

两边的算法骨架相同：右端每进入一个位置，就把 `|s[right] - t[right]|` 加进窗口代价；代价超过 `maxCost` 时，左端一直右移，直到窗口重新合法；随后用窗口长度更新答案。

区别主要是代码组织。我的版本又在 `equalSubstring` 里套了一层 `solve`，把三个参数原样再传一遍，多了一层不必要的间接；收录题解直接在当前方法里完成滑窗。窗口长度两处分别写 `i - left + 1` 和 `right + 1 - left`，只是加法顺序不同，结果一样。

两份代码都用 `for right, x in enumerate(s)`，但后面一直用 `s[right]`，`x` 没有参与计算。行为不受影响，不过写成 `range(len(s))` 会更直接。

时间复杂度都是 O(n)：右指针走 n 步，左指针在一整趟里也最多走 n 步；额外空间是 O(1)。

## 复盘

- **核心思路**：先把每一对字符的修改代价看成一个数组，问题就变成「和不超过 `maxCost` 的最长连续子数组」；用不定长滑窗维护当前代价，超出预算就收缩左端。
- **踩的坑**：① 又给滑窗多套了一层 `solve`；② `enumerate(s)` 得到的字符 `x` 没有使用；③ 窗口长度虽然写对了，但 `i - left + 1` 比 `i + 1 - left` 更容易读成「右端点 − 左端点 + 1」。
- **学到的**：① 题目没直接给数组时，可以先把每个位置转成一个数，再套已有的滑动窗口模板；② 窗口不合法时直接写 `cost > maxCost`，这个条件本身就是收缩依据；③ 收缩结束后的窗口一定合法，可以立刻更新最长长度。
- **关联问题**：LC0003、LC3634（都属于「越短越合法 / 求最长」的不定长滑窗）。

## 复习记录

| 日期 | 次数 | 结果 |
| --- | --- | --- |
| 2026-10-20 | 1 | 首次 AC |

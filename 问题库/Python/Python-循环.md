---
分类: Python
ask_count: 4
appear_count: 0
status: 已解决
created: 2026-08-29
updated: 2026-09-22
---

# Python 循环

## 停止循环

`break` 完全退出循环；`continue` 只跳过当前这一次。

```python
for i in range(5):
    if i == 2:
        break       # i=2 时退出整个循环
    print(i)        # 只打印 0, 1

for i in range(5):
    if i == 2:
        continue    # i=2 这次跳过，不打印
    print(i)        # 打印 0, 1, 3, 4
```

### 提问记录

| 日期 | 来源题目 | 解答要点 |
| --- | --- | --- |
| 2026-08-29 | 无 | `break` 退出整个循环，`continue` 跳过当前这次 |
| 2026-08-30 | 无 | 嵌套循环里 `break` 只结束所在层（内层），外层继续 |

嵌套循环中 `break` 只结束它所在的那一层（最内层），外层不受影响。

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break       # 只结束内层循环
        print(i, j)     # 外层 i 继续
```

## while 条件与变量位置

`while` 后面跟条件，条件为 True 就继续循环；变量定义在循环外（`while` 之前），否则每轮被重置。

```python
i = 0           # 变量定义在循环外
while i < 3:    # 条件：i < 3 为 True 时继续
    print(i)
    i += 1      # 每轮更新，否则死循环
```

### 提问记录

| 日期 | 来源题目 | 解答要点 |
| --- | --- | --- |
| 2026-08-30 | 无 | `while` 后面是条件，True 继续；变量定义在循环外，循环内每轮更新 |

## 循环里同时取下标（enumerate）

`enumerate` 把可迭代对象包成「带下标的迭代器」，遍历时同时拿到下标和元素。

```python
s = "abc"
for i, c in enumerate(s):
    print(i, c)     # 依次输出 0 a、1 b、2 c
```

它每轮产出的其实是一个二元组 `(下标, 元素)`，`i, c` 只是把这个元组解包到两个变量；所以只想要下标时也能写 `for pair in enumerate(s)` 再取 `pair[0]`，只是可读性差。

手工维护下标是等价写法，但要多算一次索引：

```python
for i in range(len(s)):
    c = s[i]        # 效果同上，语义不如 enumerate 直接
```

几个要点：

- `enumerate(s, 1)` 从 1 开始编号，默认 `start=0`。
- 只要下标不取值写 `for i, _ in enumerate(s)`；只要值就直接 `for c in s`，这时用 `enumerate` 属于多余。
- `s` 可以是字符串、列表、元组、字典（遍历键）等任意可迭代对象。

### 提问记录

| 日期 | 来源题目 | 解答要点 |
| --- | --- | --- |
| 2026-09-22 | 无 | `enumerate` 边遍历边给下标，产出二元组再解包；`enumerate(s, 1)` 指定起始编号 |

---
分类: Python
ask_count: 2
appear_count: 0
status: 已解决
created: 2026-08-30
---

# Python 字符串

## 字母与 ASCII 互转

字母转 ASCII 用 `ord(字符)`，ASCII 转字母用 `chr(数字)`。

```python
print(ord('a'))   # 97
print(ord('A'))   # 65
print(chr(97))    # 'a'
print(chr(65))    # 'A'
```

整个字符串逐个转：字符串 → ASCII 列表用 `[ord(c) for c in s]`；ASCII 列表 → 字符串用 `''.join(chr(n) for n in nums)`。

```python
s = "abc"
nums = [ord(c) for c in s]       # [97, 98, 99]

nums = [97, 98, 99]
s = ''.join(chr(n) for n in nums)  # 'abc'
```

### 提问记录

| 日期 | 来源题目 | 解答要点 |
| --- | --- | --- |
| 2026-08-30 | 无 | `ord()` 字母转 ASCII，`chr()` ASCII 转字母 |
| 2026-08-30 | 无 | 整串用列表推导 `[ord(c) for c in s]`；反向 `''.join(chr(n) for n in nums)` |

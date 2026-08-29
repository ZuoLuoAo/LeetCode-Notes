---
分类: Python
ask_count: 1
appear_count: 0
status: 已解决
created: 2026-08-29
---

# Python 函数

## bool 作为返回值

函数里直接 `return True` 或 `return False`；比较表达式本身就是布尔值，可直接返回。

```python
def is_even(n):
    return n % 2 == 0      # 比较表达式直接返回 True/False

def is_positive(n):
    if n > 0:
        return True
    return False

print(is_even(4))      # True
print(is_positive(-1)) # False
```

### 提问记录

| 日期 | 来源题目 | 解答要点 |
| --- | --- | --- |
| 2026-08-29 | 无 | `return True/False`，比较表达式本身就是布尔值可直接返回 |

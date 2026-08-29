---
分类: Python
ask_count: 1
appear_count: 0
status: 已解决
created: 2026-08-29
---

# Python 集合

## 自动去重

集合 `set` 自动去重，但不保证排序；要排序去重用 `sorted(set(列表))`。

```python
lst = [3, 1, 2, 1, 3]
s = set(lst)
print(s)                    # {1, 2, 3}：去重，但顺序不保证
print(sorted(set(lst)))     # [1, 2, 3]：去重且升序
```

### 提问记录

| 日期 | 来源题目 | 解答要点 |
| --- | --- | --- |
| 2026-08-29 | 无 | `set` 自动去重但无序；`sorted(set(列表))` 去重并排序 |

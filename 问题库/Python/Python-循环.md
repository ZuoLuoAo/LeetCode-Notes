---
分类: Python
ask_count: 1
appear_count: 0
status: 已解决
created: 2026-08-29
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

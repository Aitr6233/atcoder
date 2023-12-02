# 結果
AC

# 得点
100

# コード

```
M, D = map(int, input().split())
y, m, d = map(int, input().split())

# 翌日の日にする
d += 1

# 月を超えるか否かの処理
if d > D:
    d = 1
    m += 1
    
# 歳を超えるか否かの処理
if m > M:
    m = 1
    y += 1
    
print(y, m, d)
```
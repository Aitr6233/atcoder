# 結果
AC

# 得点
100

# コード
```
n, x = map(int, input().split())
list = list(map(int, input().split()))
count = 0

for i in range(n):
  if list[i] <= x:
    count += list[i]
    
print(count)
```

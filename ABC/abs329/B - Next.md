# 結果
AC

# 得点
200

# コード
```
n = int(input())
list_a = list(map(int,input().split()))
MAX = max(list_a)
uni = []

for i in range(n):
  if list_a[i] != MAX and list_a[i] not in uni:
    uni.append(list_a[i])
    
uni = sorted(uni)
print(max(uni))
```
# 結果
AC

# 得点
100

# コード
```
n = int(input())
list_ = list(map(int,input().split()))
MIN = 0

for i in range(n):
  if list_[i]%2 == 1:
    MIN = 0
    break
  else:
    value = list_[i]
    count = 0
    while True:
      value = int(value/2)
      count += 1
      
      if value%2 == 1:
        break
    
    if MIN == 0:
      MIN = count
    elif count < MIN:
      MIN = count
      
print(MIN)
```

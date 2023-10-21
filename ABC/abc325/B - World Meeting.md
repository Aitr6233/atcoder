# 結果
AC

# 得点
250

# コード
```
n = int(input())
list_data = [list(map(int,input().split())) for i in range(n)]
MAX_count = 0

for i in range(24):
  count = 0
  for j in range(n):
      num = (list_data[j][1] + i)%24
      
      if num >= 9 and num <= 17:
          count += list_data[j][0]
          
  MAX_count = max(MAX_count, count)
    
print(MAX_count)
```

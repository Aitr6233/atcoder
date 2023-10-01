# 結果
AC

# スコア
200

# コード
```
a = int(input())
b = int(input())
c = int(input())
x = int(input())
count = 0

for i in range(a+1):
  if i*500 > x:
    break 
  for j in range(b+1):
    if j*100 > x:
      break 
    for k in range(c+1):
      if k*50 > x:
        break 
      
      if (500*i + 100*j + 50*k) == x:
        count += 1
        
print(count)
```

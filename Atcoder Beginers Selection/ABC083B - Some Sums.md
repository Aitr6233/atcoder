# 得点
200

# コード
```
n, a, b = map(int, input().split())
result = 0

k = 1
while k < n+1:
  sum = 0
  for i in range(len(str(k))):
    sum += int(str(k)[i])
  
  if sum >= a and sum <= b:
    result += k
  
  k += 1
print(result)
```

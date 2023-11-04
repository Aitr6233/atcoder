# 結果
AC

# 得点
200

# コード
```
B = int(input())

for i in range(1, 100):
  if i**i == B:
    print(i)
    exit()
    
print("-1")
```
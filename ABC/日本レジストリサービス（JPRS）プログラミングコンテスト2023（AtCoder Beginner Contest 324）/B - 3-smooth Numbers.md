# 結果
AC

# 得点
200

# コード
```
n = int(input())

while n%2 == 0:
    n = int(n/2)
 
while n%3 == 0:
    n = int(n/3)

if n == 1:
    print("Yes")
else:
    print("No")
```

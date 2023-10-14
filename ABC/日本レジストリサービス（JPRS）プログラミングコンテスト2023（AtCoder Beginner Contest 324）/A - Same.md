# 結果
AC

# 得点
100

# コード
```
n = int(input())
list_a = list(map(int,input().split()))
status = True

for i in range(n-1):
    if list_a[i] != list_a[i+1]:
        status = False
        break
    else:
        pass

if status:
    print("Yes")
else:
    print("No")
```

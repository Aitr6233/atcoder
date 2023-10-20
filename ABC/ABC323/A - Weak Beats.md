# 結果
AC

# 得点
100

# コード
```
s = input()
exist_0 = False

for i in range(2, 17, 2):
  if s[i-1] == "1":
    exist_0 = True
    break
  
if exist_0:
  print("No")
else:
  print("Yes")
```

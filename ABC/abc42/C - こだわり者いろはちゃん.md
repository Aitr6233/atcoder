# 得点
300

# コード
```
n, k = map(int, input().split())
D = list(input().split())

for i in range(n, 100000):
    status = False
    
    for j in range(k):
        if D[j] in str(i):
            status = True
            break
    
    if status == False:
        print(i)
        break
```

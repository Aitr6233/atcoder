# 結果
時間切れ

# 得点
350

# コード
```
n, m = map(int, input().split())
list_data = list(map(int,input().split()))
result = [0 for _ in range(n+1)]

for i in range(m):
    num = int(input())
    
    for j in range(num):
        score = list_data[j]
        
        result[score] = result[score] + 1
        
    print()
```
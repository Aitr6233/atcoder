# 結果
AC

# 得点
300

# コード
```
import bisect

n = int(input())
list_a = list(map(int,input().split()))
list_b = sorted(list_a)

# 累積和用意
mt = [0]
for i, aa in enumerate(list_b):
    mt.append(mt[i] + aa)


result = []
for i in range(len(list_a)):
    count = 0
    start_idx = bisect.bisect_right(list_b, list_a[i])
    
    try:
        _result = mt[len(mt)-1] - mt[start_idx]
    except:
        _result = 0
    
        
    result.append(_result)

for i in result:
    print(i, end=" ")     
```   
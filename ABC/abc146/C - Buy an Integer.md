# 得点
300

# コード
```
A, B, X = map(int, input().split())

# 値段計算
def value(n):
    return A*n + B*len(str(n))
    
# 二分探索
def binary_search(n, k):
    right = n+1
    left = 0
    
    while right - left > 1:
        mid = (left + right)//2
        
        if  value(mid) <= k:
            left = mid
        else:
            right = mid
            
    return left

print(binary_search(10**9, X))
```

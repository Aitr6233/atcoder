# 得点
300

# コード
```
n, q = map(int, input().split())
list_a = list(map(int, input().split()))
list_a = sorted(list_a)

def binary_search_lower(A, n, k):
    # 探索範囲
    left = 0
    right = n
    
    # 探索範囲を狭めていく
    while left < right:
        # 探索範囲の中央
        mid = (left + right)//2
        
        if A[mid] < k:
            # a[0] ~ a[mid] は k 未満なので調べる必要が無い
            left = mid+1
        else:
            right = mid
    return n - right

for i in range(q):
    x = int(input())
    print(binary_search_lower(list_a, n, x))
    
```

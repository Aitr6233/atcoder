def binary_search(A, n, k):
    right = n
    left = -1
    
    while right - left > 0:
        mid = (left + right)//2
        
        if A[mid] == k:
            return True
        elif A[mid] > k:
            right = mid
        else:
            left = mid
            
    return False

"""
配列A [ 1, 1, 1, 2, 2, 3, 3, 3, 3, 5 ] 
順番i [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

ex ) key = 3の時

lowerは4と5の間（重複している数字の先頭）
upperは8と9の間（重複している数字の末尾）
"""
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

def binary_search_upper(A, n, k):
    # 探索範囲
    left = 0
    right = n
    
    # 探索範囲を狭めていく
    while left < right:
        # 探索範囲の中央
        mid = (left + right)//2
        
        if A[mid] <= k:
            # a[0] ~ a[mid] は k 以下なので調べる必要が無い
            left = mid+1
        else:
            right = mid
    return right
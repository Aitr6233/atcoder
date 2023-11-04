# 結果
sample<br>
・AC * 3 <br>
<br>
All<br>
・AC * 9 <br>
・WA * 27 <br>

# 得点
0/300

# コード
```
n, m = map(int, input().split())
list_a = list(map(int, input().split()))
list_a = sorted(list_a)

left = 0
right = n
MAX = 0

while right - left > 1:
    res = []
    mid = (left+right)//2
    
    for i in range(n):
        if mid <= list_a[i] < mid+m:
            res.append(list_a[i])

    if len(res) >= mid:
        left = mid
    else:
        right = mid
        
print(left)
```

# 振り返り
二分探索でいけるのはすぐに気づけた。でも実装完成までに至らなかった。<br>
範囲が指定されていないxについてどのように扱えばよいかがわからなかった。<br>

# 結果
AC

# 得点
200

# コード
```
N, S, M, L = map(int, input().split())

result = []

for s in range(0, 30):
    for m in range(0, 30):
        for l in range(0, 30):
            if 6*s + 8*m + 12*l >= N:
                sum = s*S + m*M + l*L
                result.append(sum)
                
print(min(result))
```

# 反省
全探索で、取りうる値が無限の時に最低限の全探索ではなく<br>
少し冗長に全探索をすると確実。<br>
今回の場合Nが100までだったので、<br>
s, m, lをそれぞれ(0, 17), (0, 13), (0, 9)としていたが<br>
それだとなぜか一問だけWAが出てた。<br>
しかし全部(0, 30)まで増やして全探索したらACを取れた。<br>
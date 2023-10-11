# 結果
TLE

# 得点
300

# コード
```
n = int(input())
First_class = []
Second_class = []

for i in range(n):
  class_num, score = map(int, input().split())
  gakuseki_num = i+1
  
  if class_num == 1:
    First_class.append([gakuseki_num, score])
  else:
    Second_class.append([gakuseki_num, score])
    
q = int(input())
for i in range(q):
  MIN, MAX = map(int, input().split())
  First_class_sum = 0
  Second_class_sum = 0
  
  # 1組での計算
  for j in range(len(First_class)):
    if MIN <= First_class[j][0] and First_class[j][0] <= MAX:
      First_class_sum += First_class[j][1]
    
  # 2組での計算
  for j in range(len(Second_class)):
    if MIN <= Second_class[j][0] and Second_class[j][0] <= MAX:
      Second_class_sum += Second_class[j][1]
      
  # 結果出力
  print(First_class_sum, end=" ")
  print(Second_class_sum)
```

# 反省
愚直にやるやり方としては合ってると思う。しかし計算量がオーバーしてしまう。<br>

＜ポイント＞
区間和は累積和 -> R~L番目までの和 = S_L(L番目までの和) - S_R-1(R-1番目までの和) <br>

番目までの足算を一つずつ加算せず、一回の引き算で求められる。<br>

# 改善コード
```
n = int(input())
First_class = [0]*100002
Second_class = [0]*100002

# 累積和
sum1 = [0]*100002
sum2 = [0]*100002

for i in range(n):
  class_num, score = map(int, input().split())
  
  if class_num == 1: 
    First_class[i] = score
    sum1[i] = score
  else: 
    Second_class[i] = score
    sum2[i] = score
  

for i in range(1, n+1):
  sum1[i] = sum1[i] + sum1[i-1]
  sum2[i] = sum2[i] + sum2[i-1]
  
    
q = int(input())
for i in range(q):
  L, R = map(int, input().split())
  L = L-1
  R = R-1
  
  First_class_sum = 0
  Second_class_sum = 0
  
  # 1組での計算
  First_class_sum = sum1[R] - sum1[L-1]
    
  # 2組での計算
  Second_class_sum = sum2[R] - sum2[L-1]
      
  # 結果出力
  print(First_class_sum, end=" ")
  print(Second_class_sum)
```

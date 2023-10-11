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
愚直にやるやり方としては合ってると思う。しかし計算量がオーバーしてしまう。

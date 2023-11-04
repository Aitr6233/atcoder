# 結果
sample<br>
・AC * 3 <br>
<br>
All<br>
・AC * 26 <br>
・WA * 5 <br>

# 得点
0/250

# コード
```
list_a = [list(map(int,input().split())) for i in range(9)]

def check():
  
  # 条件1のチェック
  for i in range(9):
    count = 0
    
    for j in range(9):
      count += list_a[i][j]
      
    if count != 45:
      return False
  
  # 条件2のチェック
  for i in range(9):
    count = 0
    
    for j in range(9):
      count += list_a[j][i]
      
    if count != 45:
      return False
      
  # 条件3のチェック
  for i in range(0, 9, 3):
    for j in range(0, 9, 3):
      count = 0
      
      count += list_a[i][j]
      count += list_a[i][j+1]
      count += list_a[i][j+2]
      
      count += list_a[i+1][j]
      count += list_a[i+1][j+1]
      count += list_a[i+1][j+2]
      
      count += list_a[i+2][j]
      count += list_a[i+2][j+1]
      count += list_a[i+2][j+2]
      
      if count != 45:
        return False
  
  return True
  
if check():
  print("Yes")
else:
  print("No")
```

# 反省

全探索でいけることはわかった。<br>
「区間の数字が、重複無しで1~9までの数字しかない」というのを<br>
「1~9までの総和45になる」という解釈をした。<br>
しかし、これでは1, 2, 3, ..., 9の数列の3から1をもらって1に足した時の数列<br>
2, 2, 1, ..., 9 でも成り立ってしまう。<br>
本番では、これに気づかず沼にハマってしまった。<br>
必要条件であると気づくことができなかった、反例が思いつかなかったのが悔しい。<br>
81マス分に9通りの重複チェックの全探索をしても間に合ったのに、途中で方針変更もしなかったのが悔しい。<br>


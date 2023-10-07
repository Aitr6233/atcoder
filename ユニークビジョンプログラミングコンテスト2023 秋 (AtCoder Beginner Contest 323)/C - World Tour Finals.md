# 結果
WA

# 得点
250

# コード
```
n, m = map(int, input().split())
score_list = list(map(int,input().split()))
score_result = []
yet_pb = []

for i in range(n):
  s = input()
  score = 0
  yet = []
  
  # 解けた問題分
  for j in range(m):
    if s[j] == "o":
      score += score_list[j]
    else:
      yet.append(j)
  
  # エントリーナンバー分
  score += (i+1)
  score_result.append(score)
  
  # まだ解いてない問題情報
  yet_pb.append(yet)
  

first_score = max(score_result)
for i in range(n):
  score = score_result[i]
  sub_first = first_score - score
  
  if sub_first == 0:
    print("0")
  else:
    entry_number = i+1
    print("エントリーナンバー:" + str(entry_number))
    print("点数:" + str(score_result[i]))
    yet_score = []
    
    print("未回答問題番号リスト:")
    print(yet_pb[i])
    
    for j in range(len(yet_pb[i])):
      yet_score.append(score_list[yet_pb[i][j]])
    
    print("未回答問題配点リスト:")
    print(yet_score)
    pb_count = 0
    # yet_score = sorted(yet_score)
    yet_score = list(reversed(yet_score))
    for j in range(len(yet_score)):
      print(pb_count)
      
      if score_result[i] + yet_score[j] <= first_score:
        pb_count += 1
        continue
      else:
        pb_count += 1
        break
      
    print(pb_count)
    
print(first_score)
```


# 再提出したやつ
```
n, m = map(int, input().split())
score_list = list(map(int,input().split()))
score_result = []
yet_pb = []

for i in range(n):
  s = input()
  score = 0
  yet = []
  
  # 解けた問題分
  for j in range(m):
    if s[j] == "o":
      score += score_list[j]
    else:
      yet.append(j)
  
  # エントリーナンバー分
  score += (i+1)
  score_result.append(score)
  
  # まだ解いてない問題情報
  yet_pb.append(yet)
  

first_score = max(score_result)
for i in range(n):
  score = score_result[i]
  sub_first = first_score - score
  
  if sub_first == 0:
    print("0")
  else:
    entry_number = i+1
    yet_score = []
    
    for j in range(len(yet_pb[i])):
      yet_score.append(score_list[yet_pb[i][j]])
    
    
    pb_count = 0
    yet_score = list(reversed(yet_score))
    
    for j in range(len(yet_score)):
      
      if score_result[i] + yet_score[j] <= first_score:
        pb_count += 1
        score_result[i] = score_result[i] + yet_score[j]
        continue
      else:
        pb_count += 1
        break
      
    print(pb_count)
    
```

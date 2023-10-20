# 結果
AC

# 得点
200

# コード
```
n = int(input())
result_list = [input() for i in range(n)]
result_list_num = []

for i in range(n):
  s = result_list[i]
  round_count = 0
  
  for j in range(len(s)):
    if s[j] == "o":
      round_count += 1
      
  result_list_num.append(round_count)
  
final_result = ""
for i in range(n):
  idx = result_list_num.index(max(result_list_num))
  final_result += str(idx+1)
  
  if i != n-1:
    final_result += " "
  else:
    pass
  result_list_num[idx] = -1
  
print(final_result)
```

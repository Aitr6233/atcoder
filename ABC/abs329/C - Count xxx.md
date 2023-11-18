# 結果
AC

# 得点
300

# コード
```
n = int(input())
s = input()

# 出現する文字の種類の列
unique_alp = list(set(s))
# 1種類の時用の最後尾列
c = unique_alp[-1]
c_num = ord(c)

if c_num == 122:
  c_num -= 1
else:
  c_num += 1

s += chr(c_num)
each_count = [0 for _ in range(len(unique_alp))]
  
  
# print(each_count, unique_alp)
count = 1
for i in range(n):
  if s[i] == s[i+1]:
    count += 1
  else:
    each_count[unique_alp.index(s[i])] = max(count, each_count[unique_alp.index(s[i])])
    # print(each_count, unique_alp)

    count = 1
    
result = 0
for i in each_count:
  result += i
  
print(result)

```
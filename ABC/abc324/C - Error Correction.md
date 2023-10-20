# 結果
sample <br>
・AC × 3<br>

ALL <br>
・AC × 11 <br>
・WA × 14 <br>
・TLE × 7 <br>

# 得点
0/300

# コード
```
n, T = input().split()
count = 0
result = []

for i in range(int(n)):
    s = input()
    
    if len(s) == len(T):
        can_count = True
        no_count = 0
        for j in range(len(s)):
            if no_count == 2:
                can_count = False
                break
            
            if s[j] != T[j]:
                no_count += 1
            
        if can_count:
            count += 1
            result.append(i+1)
        else:
            continue
    else:
        st = []
        for j in range(len(s)):
            st.append(s[j])
        
        if len(T) - len(st) == 1:
            count += 1
            result.append(i+1)
            continue
        
        for j in range(len(T)):
            try:
                st.remove(T[j])
            except :
                pass
        
        if len(st) == 1:
            count += 1
            result.append(i+1)
            
print(count)
print(*result)
```

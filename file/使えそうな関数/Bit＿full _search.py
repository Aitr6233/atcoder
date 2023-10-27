from itertools import product

n = int(input())
for pro in product((0, 1), repeat=n):
    
    for i in range(n):
        
        # pro[j] が1だったら処理をする
        if pro[i] == 1:
            # 処理内容
            pass
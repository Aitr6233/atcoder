from collections import deque
import pprint

# BFS関数
def bfs(start_x, start_y):
    que = deque()
    que.append((start_x, start_y))
    
    while que:
        next_x, next_y = que.popleft()
        
        for ni, nj in neighbor8(next_x, next_y):
            if not seen[ni][nj] and S[ni][nj] == '#':
                seen[ni][nj] = True
                que.append((ni, nj))
            
            
# 隣接する8頂点のリスト
def neighbor8(i, j):
    lst = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == dj == 0: continue
            if 0 <= i + di < H and 0 <= j + dj < W:
                lst.append((i + di, j + dj))
    return lst

# 入力
H, W = map(int, input().split())
S = [input() for _ in range(H)]

# 処理内容
seen = [[False] * W for _ in range(H)]  # 探索済みのマスならTrue
ans = 0
for i in range(H):
    for j in range(W):
        if not seen[i][j] and S[i][j] == '#':
            bfs(i, j)
            pprint.pprint(seen)
            ans += 1
print(ans)
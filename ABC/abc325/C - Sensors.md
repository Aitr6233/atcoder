# 結果
時間切れ

# 得点
300

# コード
```
H, W = map(int, input().split())
list_map = [input() for i in range(H)]
twoD_list = [[0 for j in range(W+2)] for i in range(H+2)]
count = 0

for i in range(H):
    for j in range(W):
        if list_map[i][j] == "#":
            count += 1
            twoD_list[i+1][j+1] = count
          
    
print(twoD_list)
    
    
class UnionFind():
    
    def __init__(self, max_size: int):
        # 要素の数分だけ配列を作る。最初は全要素がそれぞれ根である。
        self.parent = [i+1 for i in range(max_size)]
    
    # あるxの根の値を探す関数
    def find_root(self, x):
        # xの根がx, すなわち自分が根なら自分の値を返す。
        if self.parent[x] == x:
            return x
        # 自分が根じゃない時は、再帰的に自分の根はどれかをチェックする。
        else:
            self.parent[x] = self.find_root(self.parent[x])
            return self.parent[x]
        
    # 新しく結合を定義する
    def linking(self, x1, x2):
        # 根が一致していたら何もしない
        if self.find_root(x1) == self.find_root(x2):
            return
        # 根が違う場合、x2の根をx1の根にする
        else:
            self.parent[self.parent[x2]] = self.parent[x1]
            
    # 二つの値の根が同じかどうか判定する
    def check_link(self,x1, x2):
        # 根が一位しているならばTrue
        if self.find_root(x1) == self.find_root(x2):
            return True
        # 根が一致していないならばFalse
        else:
            False
            
uf = UnionFind(count)
print(uf.parent)

num = [False for i in range(count)]
for i in range(1, H+1):
    for j in range(1, W+1):
        if twoD_list[i][j] > 0:
            
            if twoD_list[i+1][j] > 0 or twoD_list[i-1][j] > 0 or twoD_list[i][j-1] > 0 or twoD_list[i][j+1] > 0 or twoD_list[i-1][j-1] > 0 or twoD_list[i+1][j+1] > 0 or twoD_list[i+1][j-1] > 0 or twoD_list[i-1][j+1]:
                pass
```

# 振り返り
グラフの連結成分の個数を求める問題というのはわかって、UnionFind木をやれば良いのかなと方針を立てたが<br>
その後はうまくやり方が思いつかず、時間切れ。<br>
解説ではBFSやDFSで探索を行う内容だった。<br>
まだ演習が足りていないことと、BFSとDFSについて理解できていないことが今回解けなかった原因なので<br>
abcの過去問のC問題の数をこなして、必要なアルゴリズムの知識を埋めていこうと思う。<br>

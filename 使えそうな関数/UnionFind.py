class UnionFiind():
    
    def __init__(self, max_size: int):
        # 要素の数分だけ配列を作る。最初は全要素がそれぞれ根である。
        self.parent = [i for i in range(max_size)]
    
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
            
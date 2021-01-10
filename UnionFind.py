class UnionFind:
    p = []

    def __init__(self, n):
        self.p = [-1] * (n+1)

    def find(self, x):
        if self.p[x] < 0:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if self.is_same(x,y):
            return False
        else:
            if self.size(x) < self.size(y):
                x,y = y, x
            self.p[x] += self.p[y]
            self.p[y] = x
            return True

    def is_same(self,x,y):
        return self.find(x) == self.find(y)

    def size(self,x):
        return -self.p[x]

    def print(self):
        print(self.p)
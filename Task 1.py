class Stakes:

    def __init__(self, height, stakes, trees):
        self.N = height
        self.M = stakes
        self.H = trees
        self.trees = 0

    def cut_down_trees(self):
        while self.M > 0:
            count = self.H // self.N
            self.M -= count
            self.trees += 1
        return f"{self.trees} Trees we need"


n = int(input("enter the height of the stockade: "))
m = int(input("enter the number of stakes: "))
h = int(input("enter the height of trees: "))
Gvidon = Stakes(n, m, h)
print(Gvidon.cut_down_trees())

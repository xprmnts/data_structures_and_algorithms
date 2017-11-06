# python3

import sys

class DSet(object):

    def __init__(self, n, lines):
        self.n = n
        self.lines = [0] + lines
        self.rank = [0] * (n + 1)
        self.parent = list(range(0, n + 1))

    def GetParent(self, x):
        parents = [] # parents to update
        root = x
        while root != self.parent[root]:
            parents.append(self.parent[root])
            root = self.parent[root]
        for i in parents:
            self.parent[i] = root
        return root

    def Merge(self, dest, src):
        src_root = self.GetParent(src)
        dest_root = self.GetParent(dest)

        if src_root == dest_root:
            return

        if self.rank[src_root] >= self.rank[dest_root]:
            self.parent[src_root] = dest_root
        else:
            self.parent[dest_root] = src_root
            if self.rank[src_root] == self.rank[dest_root]:
                self.rank[src_root] += 1

        self.lines[dest_root] += self.lines[src_root]
        self.lines[src_root] = 0

        if max(self.lines) < self.lines[dest_root]:
            max(self.lines) = self.lines[dest_root]

    def GetMaxLines(self):
        return max(self.lines)


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    arr = map(int, sys.stdin.readline().split())
    lines = list(arr)

    dset = DSet(n, lines)
    for i in range(m):
        dest, src = map(int, sys.stdin.readline().split())
        dset.Merge(dest, src)
        print(dset.GetMaxLines())

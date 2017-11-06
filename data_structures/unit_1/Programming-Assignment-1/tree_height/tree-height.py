# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def __init__(self):
        self.n = 0
        self.parent = []
        self.temp = []

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.temp = [0] * self.n

    def length(self, node_id):
        parent = self.parent[node_id]
        if parent == -1:
            return 1

        if self.temp[node_id]:
            return self.temp[node_id]

        self.temp[node_id] = 1 + self.length(self.parent[node_id])
        return self.temp[node_id]

    def compute_height(self):
        """Computes the tree height."""
        return max([self.length(_) for _ in range(self.n)])


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()

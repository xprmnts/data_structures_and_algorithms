# Uses python3
import sys


def optimal_weight(W, w):
    matrix = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            matrix[i][j] = matrix[i - 1][j]
            if w[i - 1] <= j:
                temp = matrix[i - 1][j - w[i - 1]] + w[i - 1]
                if temp > matrix[i][j]:
                    matrix[i][j] = temp
    return matrix[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

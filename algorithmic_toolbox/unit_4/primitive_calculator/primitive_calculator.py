# Uses python3
import sys


def optimal_sequence(n):
    hops = [0] * (n + 1)

    for i in range(2, n+1):
        p_one = hops[i-1]
        x_two = sys.maxsize
        x_three = sys.maxsize

        if i % 2 == 0:
            x_two = hops[i//2]
        if i % 3 == 0:
            x_three = hops[i//3]
        min_hop = min(p_one, x_two, x_three)

        hops[i] = min_hop + 1

    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 != 0 and n % 2 != 0:
            n = n - 1
        elif n % 3 == 0 and n % 2 == 0:
            n = n // 3
        elif n % 3 == 0:
            if hops[n-1] < hops[n//3]:
                n = n - 1
            else:
                n = n // 3
        else:
            if hops[n-1] < hops[n//2]:
                n = n - 1
            else:
                n = n // 2
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
# optimal_sequence(n)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # write your code here
    mid = (left + right - 1) // 2 + 1
    majority = (right - left) // 2

    l_part = get_majority_element(a, left, mid)
    r_part = get_majority_element(a, mid, right)

    l_count = 0
    for i in range(left, right):
        if a[i] == l_part:
            l_count += 1
    if l_count > majority:
        return l_part

    r_count = 0
    for i in range(left, right):
        if a[i] == r_part:
            r_count += 1
    if r_count > majority:
        return r_part

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

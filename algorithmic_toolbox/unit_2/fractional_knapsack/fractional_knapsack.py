# Uses python3
import sys

def find_max_index(weights, values, n):
  # create new array ov value per weight
    v_per_w = []
    if n == 1:
        if weights[0] == 0:
            v_per_w.append(0)
        else:
            v_per_w.append(values[0] / weights[0])
    else:
        for i in range(0, n):
            if weights[i] == 0:
                v_per_w.append(0)
            else:
                v_per_w.append(values[i] / weights[i])
    return v_per_w.index(max(v_per_w)), max(v_per_w)

def get_optimal_value(n, capacity, weights, values):
    value = 0.
    # write your code here
    for i in range(n):
        g_i, v_per_w = find_max_index(weights, values, n)
        if capacity == 0:
            return value
        a = min(weights[g_i], capacity)
        value += a * v_per_w
        weights[g_i] -= a
        capacity -= a
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))

    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    opt_value = get_optimal_value(n, capacity, weights, values)
    print("{:.10f}".format(opt_value))

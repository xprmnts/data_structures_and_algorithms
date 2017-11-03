# Uses python3
import sys

def get_optimal_value(n, capacity, weights, values):
    value = 0.
    # write your code here
    # create new array ov value per weight
    v_per_w = []
    for i in range(0, n):
        v_per_w.append (values[i]/weights[i])

    while capacity > 0:
      g_i = v_per_w.index(max(v_per_w))
      if capacity >= weights[g_i]:
        capacity -= weights[g_i]
        value += values[g_i]
        weights.remove(weights[g_i])
        values.remove(values[g_i])
        v_per_w.remove(max(v_per_w))
      else:
        value += values[g_i] * (capacity / weights[g_i])
        capacity = 0
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))

    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    opt_value = get_optimal_value(n, capacity, weights, values)
    print("{:.10f}".format(opt_value))

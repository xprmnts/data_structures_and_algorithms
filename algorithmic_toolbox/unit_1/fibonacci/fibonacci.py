# Uses python3
def calc_fib(n):
    fibo = [0, 1]
    while len(fibo) <= n:
        curr_num = fibo[-2] + fibo[-1]
        fibo.append(curr_num)
    return fibo[n]

n = int(input())
print(calc_fib(n))

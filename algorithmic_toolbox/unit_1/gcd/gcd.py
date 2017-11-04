#Uses python3
def gcd(a, b):
    if b == 0:
        return a
    elif b == 1:
        return b
    else:
        return gcd(b, a % b)


data = input()
a, b = map(int, data.split())
print(gcd(a, b))

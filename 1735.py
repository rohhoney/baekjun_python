import math
a, b = map(int, input().split())
c, d = map(int, input().split())
e = b * d
f = (a*d + c*b)

efgcd = math.gcd(e,f)
e = e//efgcd
f = f//efgcd
print(f, e)
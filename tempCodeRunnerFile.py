import math

numOfTestCase = int(input())
for i in range (0, numOfTestCase):
    a, b = input().split()
    print(a*b/math.gcd(a,b))

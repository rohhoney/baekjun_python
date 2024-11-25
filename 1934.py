import math

numOfTestCase = int(input())
for i in range (0, numOfTestCase):
    a, b = map(int,input().split())
    print(int(a*b/math.gcd(a,b)))



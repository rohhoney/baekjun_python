numberOfA, numberOfB = input().split()

A = set(input().split())
B = set(input().split())

result1 = A-B
result2 = B-A

print(len(result1)+len(result2))


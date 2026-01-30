import sys

n=int(sys.stdin.readline())
members=[list(map(lambda x:int(x) if x.isdigit() else x, sys.stdin.readline().split())) for i in range(n)]
members.sort(key=lambda member:member[0])

for member in members:
    print(*member)
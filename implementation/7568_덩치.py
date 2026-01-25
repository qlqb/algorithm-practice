import sys

n=int(sys.stdin.readline())
people=[tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    rank=1
    for person in people:
        if people[i][0]<person[0] and people[i][1]<person[1]:
            rank+=1
    print(rank, end=' ')
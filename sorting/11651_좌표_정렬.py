import sys

n=int(sys.stdin.readline())
coordinates=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
coordinates.sort(key=lambda coordinate: (coordinate[1], coordinate[0]))

for x,y in coordinates:
    print(x,y)
import sys

n=int(sys.stdin.readline())
cnt=0

while n:
    n//=5
    cnt+=n

print(cnt)
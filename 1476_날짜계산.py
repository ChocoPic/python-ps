# ~15 ~28 ~19
# 1 16 16 -> 16
# 19 -> 4 19 19
# 20 -> 4 20 1

# S를 기준으로 돌려보자
# i=0 -> 현재 : S + i*0년 => %15==E and %19==M

import sys
input = sys.stdin.readline

E,S,M = map(int, input().split())
i=0
while(True):
    year = S + 28*i
    if year%15==E%15 and year%19==M%19:
        break
    i += 1
print(year)
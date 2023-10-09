# i(1~1,000,000)를 약수로 갖는 수를 
# 인덱스i에 더해주는 방식으로 f(n)을 구한다
# i*j에 +i 해주는 것
# g(n) = g(n-1) + f(n)

import sys
input = sys.stdin.readline

MAX = 1000000   # n: 1~1,000,000
F = [1] * (MAX+1)
G = [0] * (MAX+1)
### F(n) 리스트 채우기
for i in range(2, MAX+1):
    for j in range(1, MAX//i+1):
        F[i*j] += i
### G(n) 리스트 채우기
for i in range(1, MAX+1):
    G[i] = G[i-1] + F[i]
### 정답 출력하기  
t = int(input())
for _ in range(t):
    print(G[int(input())])
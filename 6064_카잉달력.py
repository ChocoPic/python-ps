'''
x=i%M+1, y=i%N+1
1씩 더하기 했는데 시간초과가 난다. 더 간단한 식은?
### k = x+iM = y+jN 인 k 값을 찾아야한다.
### k-x = iM, k-y = iN이니까 (k-x)%M==0 and (k-y)%N==0 인 k를 찾는 것이다
# k는 어차피 x나y보다 크거나 같을테니 k=x로 초기화한다
# k+=1을 해도 되지만 시간을 위해 k = x+iM이니까 M씩 더하자.
'''

import sys
input = sys.stdin.readline

def solve(M,N,x,y):
    k = x
    while k <= M*N: # 대충 M*N번
        if (k-x)%M==0 and (k-y)%N==0:
            return k
        k+=M
    return -1
T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(solve(M,N,x,y))
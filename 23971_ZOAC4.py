'''
0   2   4
2 
4
: 5/(1+1)  올림
4/(1+1)   올림

0   2   4   6
3
6
9
: 10, 7 / 3 2
10/4 -> 4
7/3 -> 4
'''
import math
H,W,N,M = map(int, input().split())
a = math.ceil(H/(N+1))
b = math.ceil(W/(M+1))
print(a*b)
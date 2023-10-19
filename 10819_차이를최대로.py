import sys
input = sys.stdin.readline
N = int(input())    #3~8
A = list(map(int, input().split())) #-100~100

#모든 조합 만들어보고 max값 찾기
from itertools import permutations

max_result = 0
p_list = list(permutations(A, N))
for pp in p_list:
    result = 0
    for i in range(N-1):
        p = list(pp)
        result += abs(p[i]-p[i+1])
        i+=1
    if result > max_result:
        max_result = result
print(max_result)
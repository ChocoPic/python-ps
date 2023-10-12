'''
5 3 1 4 2
5 3 2 1 4 : 1을2로, 뒷쪽 오름차순
5 3 2 4 1 : 1<->4
5 4 1 2 3 : 3을4로, 뒷쪽 오름차순
3 4 5 6 7 1 2
3 4 5 6 7 2 1 : 바로앞(1)<현(2)면 swap
3 4 5 7 6 1 2 : 맨뒤부터 탐색, 바로앞(6)<현(7)이면 swap하고 뒤는 오름차순
'''
# 뒤에서부터 탐색하다가
# [i-1]<[i]를 발견하면 swap하고 [i:]은 오름차순정렬
# i가 맨끝([i]==[-1]) 이라면 정렬은 안함
# [i-1]<[i]를 발견못하면 -1

import sys
input = sys.stdin.readline
N = int(input())
p = list(map(int, input().split())) #입력 순열 1~N으로 이루어짐

for i in range(N-1, -1, -1):
    if i==0:
        print(-1)
        break
    elif p[i-1] < p[i]:
        for j in range(N-1, 0, -1): # 다음 큰수 찾기
            if p[i-1] < p[j]:
                p[i-1], p[j] = p[j], p[i-1]   #swap
                p[i:] = sorted(p[i:])  #오름차순청렬
                print(' '.join(map(str, p)))
                exit()
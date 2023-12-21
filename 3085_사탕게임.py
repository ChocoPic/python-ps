'''
1. 색이다른 인접한 두칸을 고른다
2. 두 칸의 사탕을 서로 교환한다
3. 가장긴 연속부분(행or열)을 고른다음 그 사탕을 모두 먹는다

=> 최대 N개면 N 리턴. 미만이면 가장 길게 연속인 부분을 찾고, 교환해서 더 먹을 수 있나 체크
''' 

import sys
input = sys.stdin.readline

N = int(input())
board = [list(input().strip()) for _ in range(N)]

# 최대 사탕 개수를 리턴해주는 함수
def checkMax():
    max_cnt = 1
    for i in range(N):
        # 가로 최대 개수 확인하기
        cnt = 1
        for j in range(1, N):
            if board[i][j-1] == board[i][j]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
        
        # 세로 최대 개수 확인하기
        cnt = 1
        for j in range(1, N):
            if board[j-1][i] == board[j][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
            
    return max_cnt

def swap(i1, j1, i2, j2):
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

result = 1   # 먹을 수 있는 최대 사탕 수
result = max(result, checkMax())
    
if result < N:
    for i in range(N):  #가로(i행, row)
        for j in range(N):  #세로(j열, col)
            #(가로) 
            # 1.색이 다른 인접한 두 칸을 골라 교환한다
            if j<N-1 and board[i][j] != board[i][j+1]:
                swap(i,j, i,j+1)    #교환
                result = max(result, checkMax())    # 2.가장 긴 연속부분을 고른다
                swap(i,j, i,j+1)    #원래대로
            #(세로) 
            # 1.색이 다른 인접한 두 칸을 골라 교환한다
            if i<N-1 and board[i][j]!=board[i+1][j]:
                swap(i,j, i+1,j)    #교환
                result = max(result, checkMax())    # 2.가장 긴 연속부분을 고른다
                swap(i,j, i+1,j)    #원래대로
print(result)
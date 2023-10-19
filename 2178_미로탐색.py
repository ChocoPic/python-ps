N,M = map(int, input().split())
miro = []
for i in range(N):
    miro.append(input())
    
visited = [[0]*M for _ in range(N)] #방문여부 저장
dx = [-1, 1, 0, 0]  #이동가능한 방향은 아래, 위, 왼쪽, 오른쪽
dy = [0, 0, -1, 1]

queue = [(0,0)] #시작칸 큐에 추가
visited[0][0] = 1   #시작칸 방문

while queue:    #큐가 빌때까지 반복
    x,y = queue.pop(0)  #큐에서 하나 pop
    
    if x==N-1 and y==M-1:   # (N,M) 에 도착하면 종료한다.
        print(visited[x][y])
        break
    
    for i in range(4):  #인접 칸에 대해 반복
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if visited[nx][ny]==0 and miro[nx][ny]=='1': #방문안했고, 길이면,
                visited[nx][ny] = visited[x][y]+1 #방문하고(이전칸+1 저장)
                queue.append((nx, ny))  #큐에 추가
import sys
input = sys.stdin.readline

def rotate(shape):
    w, h = len(shape[0]), len(shape)
    rotated = [[0 for _ in range(h)] for _ in range(w)] # w<->h
    for i in range(h):
        for j in range(w):
            rotated[j][h-i-1] = shape[i][j]
    return rotated
    
def flip(shape):
    flipped = [ w[::-1] for w in shape]
    return flipped

# print(shapes[0])
# print(rotate(shapes[0]))
# print(flip(shapes[0]))

### 전체 모양 만들기
shapes = [
    [[1,1,1,1]],    #ㅡ 2가지 (회전0,90)
    [[1,1,1],         #L 8가지 (회전 0,90,180,270 * 좌우대칭)
     [0,0,1]],
    [[1,1,0],         #Z 4가지 (회전 0,90 * 좌우대칭)
     [0,1,1]],
    [[1,1,1],       #ㅜ 4가지 (회전 0,90,180,270)
     [0,1,0]],
    [[1,1],         #ㅁ 1가지
     [1,1]]    
]

all_shapes = [] # 전체 모양
for i in range(len(shapes)):
    if i==0:
        all_shapes.append(shapes[0])
        all_shapes.append(rotate(shapes[0]))
    elif i==1:
        s = shapes[1]
        for _ in range(2):  #대칭
            for _ in range(4):  #회전
                s = rotate(s)
                all_shapes.append(s)
            s = flip(s)
    elif i==2:
        s = shapes[i]
        for _ in range(2):  #대칭
            for _ in range(2):   #회전
                s = rotate(s)
                all_shapes.append(s)
            s = flip(s)
    elif i==3:
        s = shapes[i]
        for _ in range(4):   #회전
            s = rotate(s)
            all_shapes.append(s)
    else:
        all_shapes.append(shapes[i])
# for s in all_shapes:
#     for ss in s:
#         print(ss)
#     print(" ")

### 검사하기
N, M = map(int, input().split())    #(4 ≤ N, M ≤ 500)
paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))

answer = 0
for shape in all_shapes:
    h,w = len(shape),len(shape[0])
    for i in range(N-h+1):  # (0,0)부터 (n-h,m-w)까지 놓아본다
        for j in range(M-w+1):
            target = [row[j:j+w] for row in paper[i:i+h]] # paper 중 올려놓은 영역
            temp = 0
            for r1, r2 in zip(shape, target):
                temp += sum([a*b for a,b in zip(r1, r2)])
            # print(shape,"-",target,temp)
            if answer < temp:
                answer = temp
            
print(answer)
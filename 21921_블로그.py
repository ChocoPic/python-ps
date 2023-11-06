import sys
input = sys.stdin.readline

N,X = map(int,(input().split()))
visit = list(map(int,input().split()))

if max(visit)==0:
    print("SAD")
    
else:
    total = sum(visit[:X])  # 첫칸 합
    max_total, max_cnt = total, 1

    for i in range(X, N):
        total += (-visit[i-X]+visit[i])    # 이전칸 첫값 빼고, 현재칸 마지막값 더함
        if total > max_total:    
            max_total = total
            max_cnt = 1
        elif total == max_total:
            max_cnt += 1

    print(max_total); print(max_cnt)
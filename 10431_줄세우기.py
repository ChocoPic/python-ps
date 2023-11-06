'''
물러서는 횟수: 자기보다 뒤에있는 애들 수
자기 다음으로 키큰애 앞에 섬
'''
P = int(input())

for _ in range(P):
    children = list(map(int, input().split()))
    l = [children[1]]   # 학생들 정렬할 리스트
    cnt = 0 # 물러난 횟수
    
    for i in range(2, len(children)):
        flag = 0
        for j in range(len(l)): # 앞에서부터 탐색해서
            if l[j] > children[i]: # 정렬된 학생 중 자기보다 큰애가 있으면
                cnt += (len(l)-j)   # 뒤 학생들은 뒤로
                l.insert(j, children[i])    # 앞에 선다
                flag = 1
                break
        if flag==0: # 자기가 제일 크면 마지막에 선다
            l.append(children[i])
    print(children[0], cnt)
                 
# 앞에서부터. i빼고
    # i를 제외하고 하나(j) 빼고
        # 다 더해서 100인지 확인
        
        
import sys
input = sys.stdin.readline
    
dwarves = []
for i in range(9):
    dwarves.append(int(input()))
dwarves.sort()

fake1 = fake2 = 0
total_height = sum(dwarves)
solved = False
for i in range(len(dwarves)):   #0~9,i=0
    fake1 = dwarves[i]  #제외할 난쟁이1
    
    for j in [x for x in range(len(dwarves)) if x!=i]:  #1~9,i=0,j=1
        fake2 = dwarves[j]  #제외할 난쟁이2
        
        if (total_height-fake1-fake2) == 100:   # 정답
            for k in range(len(dwarves)):   # 출력하기
                if k!=i and k!=j:
                    print(dwarves[k])
            solved = True
            break
        
    if solved: break
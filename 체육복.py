'''
바로 앞or뒤한테만 빌려줄 수 있음. 최대한 많은 학생이 체육복이 있어야함. 여벌이 있어야 빌려줄 수 있음
전체학생수n / 도난학생배열lost / 여벌있는학생배열reserve

reserve에 있는 학생만 빌려줄 수 있다. 근데 lost에도 있으면 못빌려준다. reserve에 없고 lost에 있으면 빌려야한다
'''

def solution(n, lost, reserve):
    # 체육복 몇 개 있는지 계산
    students = [1 for _ in range(n)]
    for l in lost:
        students[l-1] -= 1
    for r in reserve:
        students[r-1] += 1
    print(students)
    
    # 도난당한 학생들 나눠주기  
    for i in range(n):
        if students[i]==0:
            if i!=0 and students[i-1] == 2:
                students[i-1],students[i] = 1,1
            elif i!=n-1 and students[i+1] == 2:
                students[i+1],students[i] = 1,1
    
    return n-students.count(0)
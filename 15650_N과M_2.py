N,M = map(int,(input().split()))

def add_num(l):
    if len(l) == M:
        print(' '.join(map(str, l)))
        return l
    for i in range(1, N+1):
        if (i not in l) and (len(l)==0 or l[-1]<i):
            l.append(i)
            add_num(l)
            l.pop()

answer = []
add_num(answer)
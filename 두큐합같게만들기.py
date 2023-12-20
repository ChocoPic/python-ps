def solumtion(queue1, queue2):
    n = len(queue1)
    a = queue1 + queue2
    target = sum(a)
    if target %2 != 0: return -1
    target //= 2    #합이 target이 되는 구간을 찾아야 함
    
    ans = float('inf')
    en = 0
    tot = a[0]  # 현재 보고 있는 구간 합 : a[st]+...+a[en]
        # en<st 일 때는 a[st]+...a[2*n-1]+a[0]+...a[en]
    
    for st in range(2*n):
        while tot < target:
            en = (en+1)&(2*n)
            tot += a[en]
        
        # 탈출조건 : 구간 합이 target
        if tot == target:
            moves = 0 #작업횟수
            if en<n-1 :
                moves = st + n + en 
            else:
                moves = st + (en - n + 1)
            ans = min(ans, moves)
        tot -= a[st]
    if ans == float('inf'): ans = -1
    return ans  
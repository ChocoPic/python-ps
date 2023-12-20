# 입력받기
M, N = map(int, input().split())

# 소수 출력하기
for i in range(M, N+1):
    # 1은 소수가 아니므로 출력하지 않는다
    if i==1:
        continue
    
    # 2부터 i의 제곱근까지 소수인지 확인한다
    for j in range(2, int(i**0.5)+1):
        if i%j==0:  # 나누어 떨어지면 소수가 아니다
            break
    
    # 1도 아니고 나누어떨어지지 않았으니 소수. 출력한다
    else: 
        print(i)
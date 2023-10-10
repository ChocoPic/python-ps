import sys
input = sys.stdin.readline

### 소수 목록 만들기
MAX = 1000000
is_prime_list = [True for _ in range(MAX+1)]    #소수인지 담을 배열

for cur_n in range(2, int(MAX**0.5)+1):
    if is_prime_list[cur_n]:
        for mul_n in range(cur_n**2, MAX+1, cur_n):
            is_prime_list[mul_n] = False

### Goldbach's conjecture is wrong. 체크
while(True):
    n = int(input())
    if n==0:
        break
        
    solved = False
    for i in range(3, n, 2):
        if is_prime_list[i]:
            if is_prime_list[n-i]:
                print(f'{n} = {i} + {n-i}')
                solved = True
                break
    if not solved:
        print("Goldbach's conjecture is wrong.")

# b = set(i for i in range(2,1000000))
# for i in range(2,1001):
#     if i in b:
#         b.difference_update(range(i * i, 1000000 +1, i))
def is_prime(a):
    if a==1:
        return False
    for i in range(2, a):
        if a%i == 0:
            return False
    return True
    

n = int(input())
nums = list(map(int, input().split()))  #1~1000

cnt = 0
for num in nums:
    if is_prime(num):
        cnt+=1
print(cnt)